from itsdangerous import URLSafeTimedSerializer
from config.config import Config
# from flask import current_app

config = Config()

def verify_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config.SECRET_KEY)
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        return email
    except Exception as e:
        return None