#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    """
    Classe de gestion de l'authentification pour l'API.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Détermine si la route `path` nécessite une authentification.

        Actuellement, toujours retourne False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Récupère la valeur de l'en-tête Authorization à partir de la requête.

        Actuellement, retourne None.
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Retourne l'utilisateur courant en fonction de la requête.

        Actuellement, retourne None.
        """
        return None