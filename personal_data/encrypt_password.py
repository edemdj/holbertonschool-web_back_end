#!/usr/bin/env python3
""" function that expects one string argument name password
and returns a salted, hashed password, which is a byte string."""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash a password """
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check a password """
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)
