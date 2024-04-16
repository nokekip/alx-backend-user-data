#!/usr/bin/env python3
""""
Module for the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a path requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
