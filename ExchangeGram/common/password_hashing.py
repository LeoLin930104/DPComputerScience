# pip install bcrypt
import bcrypt


def gen_pwd_hsh(password: str) -> bytes:
    salt = bcrypt.gensalt()
    password = password.encode("utf8")

    hashed = bcrypt.hashpw(password=password, salt=salt).decode("UTF-8")
    return hashed