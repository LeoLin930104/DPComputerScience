# pip install bcrypt
import bcrypt


def gen_pwd_hsh(password: str) -> bytes:
    salt = bcrypt.gensalt()
    password = password.encode("utf-8")
    hashed = bcrypt.hashpw(password=password, salt=salt).decode("UTF-8")
    return hashed


def check_pwd(password: bytes, password_hash: bytes) -> bool:
    return bcrypt.checkpw(password, password_hash)