# -*- coding: utf-8 -*-
import hashlib
import bcrypt


def hash_with_bcrypt(var: str) -> str:
    if var:
        byte_var = var.encode("utf-8")
        my_salt = bcrypt.gensalt()
        return bcrypt.hashpw(byte_var, my_salt)
    return var


def hash_with_md5(var):
    return hashlib.md5(str(var).encode("utf-8")).hexdigest() if var else var
