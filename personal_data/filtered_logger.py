#!/usr/bin/env python3
"""
function called filter_datum
"""

import re
from typing import List
import logging
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """returns the log message obfuscated"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        msg = rf"{field}=[^;]+"
        message = re.sub(msg, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """returns a loggin.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to the database """
    connection = mysql.connector.connection.MySQLConnection(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return connection


def main():
    """ Main function """
    db = get_db()
    cursor = db.cursor()
    query = """
    SELECT name, email, phone, ssn, password, ip, last_login, user_agent
    FROM users;
    """
    cursor.execute(query)
    logger = get_logger()
    for row in cursor.fetchall():
        record = {
            "name": row[0],
            "email": row[1],
            "phone": row[2],
            "ssn": row[3],
            "password": row[4],
            "ip": row[5],
            "last_login": row[6],
            "user_agent": row[7],
        }
        message = "; ".join(f"{key}={value}" for key,
                            value in record.items()) + ";"
        message = filter_datum(PII_FIELDS, '***', message, '; ')
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
