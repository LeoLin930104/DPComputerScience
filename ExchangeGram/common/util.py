import re

email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
email_regex = "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"


def validate_email(email: str) -> bool:
    return re.search(email_regex, email) is not None