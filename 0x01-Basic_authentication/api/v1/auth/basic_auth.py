#!/usr/bin/env python3
"""
    Basic Auth
"""


from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
        Basic Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' def extract base64 authorization header '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' def decode base 64 authorization '''
        if base64_authorization_header and type(
                    base64_authorization_header) == str:
            try:
                x = base64_authorization_header.encode('utf-8')
                base = base64.b64decode(x)
                return base.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' return the user mail and the password '''
        c = decoded_base64_authorization_header
        if c and type(c) == str and ":" in c:
            mail = c.split(':')[0]
            password = "".join(c.split(':', 1)[1:])
            return(mail, password)
        return(None, None)
