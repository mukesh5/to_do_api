import jwt

from api.services.core.constants import SECRET_KEY


class ApiTokenUtil(object):
    @staticmethod
    def start_session(payload: dict):
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
