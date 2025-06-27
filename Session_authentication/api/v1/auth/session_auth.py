#!/usr/bin/env python3
""" Session authentication module """
from typing import TypeVar

from flask import request
from api.v1.auth.auth import Auth
import uuid
from models.user import User

class SessionAuth(Auth):
    """ SessionAuth class for session authentication mechanics """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id.
        Returns:
            Session ID as string if created, otherwise None
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retourne le user_id associé à un session_id donné."""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
    
    

    def current_user(self, request=None):
        session_id = self.session_cookie(request)
        print("session_id:", session_id)
        user_id = self.user_id_for_session_id(session_id)
        print("user_id:", user_id)
        if user_id is None:
            return None
        user = User.get(user_id)
        print("user:", user)
        return user
    
    def destroy_session(self, request=None):
        """
        Deletes the user session (logout).
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        # Suppression de la session
        del self.user_id_by_session_id[session_id]
        return True