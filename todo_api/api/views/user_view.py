from django.http import HttpRequest
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.user_models import User
from api.serializers.user_serializers import UserSerializer
from api.services.impl.user_service_impl import UserServiceImpl
from api.supportlib.utils.api_utils import ApiTokenUtil


@api_view(['POST'])
def register_user(request: HttpRequest) -> Response:
    user_service = UserServiceImpl()
    user_data = UserSerializer(data=request.data)
    if not user_data.is_valid():
        return Response(status=422, data={'message':'Please send valid data'})
    user = user_service.get_user_by_email(user_data.data.get('email'))
    if user:
        return Response(status=422, data={'User with the email already exists'})
    user = User()
    user.first_name = user_data.data.get('first_name')
    user.last_name = user_data.data.get('last_name')
    user.email = user_data.data.get('email')
    user.password = UserServiceImpl.encrypt_password(user_data.data.get('password'))
    user.created_at = datetime.now()
    user.updated_at = datetime.now()
    user = user_service.register_user(user)
    payload = {
        'id': user.id,
        'first_name': user.first_name,
        'email': user.email
    }
    token = ApiTokenUtil.start_session(payload)
    data = {
        'token': token,
        'first_name': user.first_name,
        'email': user.email
    }
    return Response(data=data)


@api_view(['POST'])
def validate_user_login(request: HttpRequest) -> Response:
    user_service = UserServiceImpl()
    email = request.data.get('email')
    password = request.data.get('password')
    if not email:
        return Response(status=422, data={'message': 'Email or password is missing'})
    if not password:
        return Response(status=422, data={'message': 'Email or password is missing'})
    user = user_service.get_user_by_email(email)
    if not user:
        return Response(status=404, data={'message': 'User Not Found'})

    validated = user_service.validate_user_by_email_and_password(email, password)
    if not validated:
        return Response(status=401, data={'message': 'Invalid credentials'})
    payload = {
        'id': user.id,
        'first_name': user.first_name,
        'email': user.email
    }
    token = ApiTokenUtil.start_session(payload)
    data = {
        'token': token,
        'first_name': user.first_name,
        'email': user.email
    }
    return Response(data=data)

