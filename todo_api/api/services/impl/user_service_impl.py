from api.models.user_models import User
from api.repositories.user_repository import UserRepository
from api.services.core.constants import ENCRYPTION_SALT
from api.services.core.user_service import UserService
import hashlib
import binascii


class UserServiceImpl(UserService):
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, user: User) -> User:
        return self.user_repository.add_user(user)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)

    @staticmethod
    def encrypt_password(password: str):
        decoded_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),
                                          ENCRYPTION_SALT, 100000)
        return binascii.hexlify(decoded_key).decode('utf-8')

    def validate_user_by_email_and_password(self, email: str, password: str) -> bool:
        encrypted_password = self.encrypt_password(password)
        user = self.user_repository.get_user_by_email_password(email, encrypted_password)
        if user:
            return True
        return False
