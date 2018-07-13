import hashlib


class PasswordHelper:
    @classmethod
    def encrypt(cls, password):
        return hashlib.md5(password.encode("utf8")).hexdigest()
