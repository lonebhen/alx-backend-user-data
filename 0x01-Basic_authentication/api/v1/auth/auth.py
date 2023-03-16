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
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path is None or excluded_paths is None:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        '''auth header'''
        return

    def current_user(self, request=None) -> TypeVar('User'):
        '''current user'''
        return
