from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto") 

def hash_pass(password):
    return pwd_context.hash(password)

def validate_password():
    pass