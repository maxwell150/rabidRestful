"""This module is for hashing passwords"""

from passlib.context import CryptContext

pswd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

               
def hash(password: str):
    return pswd_context.hash(password)
