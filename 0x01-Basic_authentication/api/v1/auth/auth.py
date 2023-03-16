#!/usr/bin/env python3
"""
    API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
        Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require auth'''
        return

    def authorization_header(self, request=None) -> str:
        '''auth header'''
        return

    def current_user(self, request=None) -> TypeVar('User'):
        '''current user'''
        return
