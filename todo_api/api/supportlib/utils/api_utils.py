import functools

import jwt
from django.http import HttpRequest

from api.services.core.constants import SECRET_KEY


class ApiTokenUtil(object):
    @staticmethod
    def start_session(payload: dict):
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token


class _AuthorizationDecorator(object):
    @staticmethod
    def generate(secret_key: str = None):
        return _AuthorizationDecorator(secret_key)

    def __init__(self, secret_key: str = None):
        self.secret_key = secret_key

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            try:
                if not self.secret_key:
                    payload = jwt.decode(request.META['HTTP_AUTHORIZATION'], SECRET_KEY,
                               algorithms=['HS256'])
                else:
                    payload = jwt.decode(request.META['HTTP_AUTHORIZATION'].split(' ')[1], self.secret_key,
                               algorithms=['HS256'])
                request.META['is_authorized'] = True
                request.META['user'] = payload['id']
            except Exception:
                request.META['is_authorized'] = False
            return func(request, *args, **kwargs)

        return wrapper


authorize = _AuthorizationDecorator.generate
