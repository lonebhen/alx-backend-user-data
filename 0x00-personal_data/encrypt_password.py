#!/usr/bin/env python3

"""
    Encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        Password hashing
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Compare if hashed password is similar to unhashed password
    """

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
