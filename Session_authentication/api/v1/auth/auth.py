#!/usr/bin/env python3
""" Authentication module for API """
from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    """
    class Auth provides methods for handling API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if the path requires authentication.
        If path is None or excluded_paths is None, returns True.
        If path is not a string or excluded_paths is not a list, returns True.
        If path ends with '/', it is stripped.
        """
        if path is None or excluded_paths is None:
            return True
        
        if not isinstance(path, str) or not isinstance(excluded_paths, list):
            return True
        
        if path.endswith('/'):
            path = path[:-1]

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]
            if path == excluded_path or path.startswith(excluded_path + '/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns the authorization header from the request.
        If the request is None or does not contain an Authorization header,
        returns None.
        """
        if request is None:
            return None
        
        if "Authorization" not in request.headers:
            return None
        
        auth_header = request.headers.get('Authorization')
        if isinstance(auth_header, str) and len(auth_header) > 0:
            return auth_header
        
        return None

    def current_user(self, request=None) -> User:
        """
        returns the current user from the request.
        If the request is None, returns None.
        This method should be overridden in a subclass to return the user
        associated with the request.
        If the request does not contain user information, returns None.
        """
        return None
