from django.urls import path

from api.views.user_view import register_user

urlpatterns = [
    path('registerUser', register_user, name="register_user")
]