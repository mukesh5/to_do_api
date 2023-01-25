from api.models.user_models import User
from django.core.exceptions import ObjectDoesNotExist


class UserRepository:
    def add_user(self, user: User) -> User:
        user.save()
        return user

    def get_user_by_email(self, email: str) -> User:
        try:
            user = User.objects.get(email=email)
            return user
        except ObjectDoesNotExist:
            return None

    def get_user_by_email_password(self, email: str, password: str) -> User:
        try:
            user = User.objects.get(email=email, password=password)
            return user
        except ObjectDoesNotExist:
            return None


