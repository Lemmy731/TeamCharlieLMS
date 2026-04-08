from itsdangerous import URLSafeTimedSerializer
from config.config import Config
# from flask import current_app

config = Config()

def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(config.SECRET_KEY)
    return serializer.dumps(email, salt='password-reset-salt')