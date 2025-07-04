#!/usr/bin/env python3
"""
Module providing user authentication functionality.
"""

import uuid

from db import DB
from user import User
from bcrypt import checkpw, hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password using bcrypt.
        """

        return hashpw(password.encode("utf-8"), gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user if the email is not already taken.
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a login attempt for a given email and password.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        hashed_password = user.hashed_password

        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode("utf-8")

        return checkpw(password.encode("utf-8"), hashed_password)

    def create_session(self, email: str) -> str:
        """
        Creates a new session ID for a user identified by their email.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieves a user based on the given session ID.
        """

        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys the session of a user.
        """

        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a reset password token for a user.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Updates a user's password.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = self._hash_password(password)

        self._db.update_user(
            user.id, hashed_password=hashed_password, reset_token=None)


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.
    """

    return hashpw(password.encode("utf-8"), gensalt())


def _generate_uuid() -> str:
    """
    Generates a new UUID string.
    """

    return str(uuid.uuid4())
