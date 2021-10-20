import random
import string
from passlib.context import CryptContext

class PasswordCrypt():
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )    
    def encrypt_password(self, password):
        """Encrypt password

        Args:
            password (string): Encrypt any string

        Returns:
            [string]: return encrypted password string 
        """
        return { 'encrypted': self.pwd_context.encrypt(password) }

    def check_encrypted_password(self, password, hashed):
        """Check if the password is well encrypted

        Args:
            password (string): - clear password 
            hashed (string): - encrypted password

        Returns:
            [bool]: return True/False
        """
        return self.pwd_context.verify(password, hashed)
    
    def generate_password(self):
        """generate custom password

        Returns:
            [dict]: - A dictionary with two key { encrypted, password }
        """
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(20))
        return { 'encrypted': self.encrypt_password(result_str), 'password': result_str }