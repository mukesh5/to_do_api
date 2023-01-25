from django.urls import path

from api.views.user_view import register_user, validate_user_login

urlpatterns = [
    path('registerUser', register_user, name="register_user"),
    path('login', validate_user_login, name="validate_login")
]
