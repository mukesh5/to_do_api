from abc import abstractmethod

from api.models.user_models import User


class UserService:
    @abstractmethod
    def register_user(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def validate_user_by_email_and_password(self, email: str, password: str) -> bool:
        raise NotImplementedError
