from api.models.user_models import User
from api.repositories.user_repository import UserRepository
from api.services.core.user_service import UserService


class UserServiceImpl(UserService):
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, user: User) -> User:
        return self.user_repository.add_user(user)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)
