#!/usr/bin/env python3
"""
Basic authentication module
"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 part from the Authorization header
        """
        if authorization_header and isinstance(
                authorization_header, str) and authorization_header.startswith(
                    "Basic "):
            return authorization_header[6:] 
