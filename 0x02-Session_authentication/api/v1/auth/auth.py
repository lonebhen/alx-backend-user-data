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
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        '''auth header'''

        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        '''current user'''
        return
