from passlib.context import CryptContext
from random import randint
from datetime import datetime
import re

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)


def validate_name(name):
    reg = "[^']{3,}?"
    compiled_reg = re.compile(reg)
    return re.search(compiled_reg, name)


def validate_password(password):
    reg = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    compiled_reg = re.compile(reg)
    return re.search(compiled_reg, password)


def encrypt_password(password):
    return pwd_context.encrypt(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def random_num_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def get_timestamp():
    timestamp = datetime.now()
    created_on = timestamp.isoformat()
    return created_on
