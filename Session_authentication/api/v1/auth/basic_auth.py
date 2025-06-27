#!/usr/bin/env python3
""" Basic Authentication module """
from api.v1.auth.auth import Auth
from typing import Tuple
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """ For the moment this class will be empty. """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
         that returns the decoded value of a Base64
         string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        that returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password


    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> User:
        """
        returns the User instance based on his email and password
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})

        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> User:
        """
        overloads Auth and retrieves the User instance for a request
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user