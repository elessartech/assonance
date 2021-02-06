from passlib.context import CryptContext
from base64 import b64encode
import base64

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
    return pwd_context.encrypt(password)

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii') 
    return render_pic