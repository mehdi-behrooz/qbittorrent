"""
    Source: https://github.com/qbittorrent/qBittorrent/blob/
            f3c0cc3cee825000f9d63cdce11398d02be6d0ed/
            src/base/utils/password.cpp
"""

import base64
import hashlib
import os

ITERATIONS = 100_000
SALT_SIZE = 16

def hash(password):

    salt = os.urandom(SALT_SIZE)
    hash = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, ITERATIONS)

    return '@ByteArray({}:{})'.format(
            base64.b64encode(salt).decode(),
            base64.b64encode(hash).decode()
        )
