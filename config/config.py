from datetime import timedelta  
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_TOKEN_LOCATION = ["cookies"]
    # JWT_TOKEN_LOCATION = ["headers"]
    JWT_COOKIE_SECURE = False
    JWT_ACCESS_COOKIE_PATH = "/api/"
    JWT_REFRESH_COOKIE_PATH = '/token/refresh'
    JWT_COOKIE_CSRF_PROTECT = True
   

    GOOGLE_CLIENT_ID=os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET=os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_DISCOVERY_URL=os.getenv('GOOGLE_DISCOVERY_URL')
    GOOGLE_REDIRECT_URI=os.getenv('GOOGLE_REDIRECT_URI')

    SECRET_KEY=os.getenv('SECRET_KEY')
    # Mail Config
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT', 587)
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False') == 'True'
    # MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False') == 'True'
    # MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') 
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    MAIL_DEBUG = True

    # AUTHORIZATION_BASE_URL=os.getenv('AUTHORIZATION_BASE_URL')
    # TOKEN_URL=os.getenv('TOKEN_URL')
    # REDIRECT_URI=os.getenv('REDIRECT_URI')

    

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'