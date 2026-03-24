from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize Flask extensions
db = SQLAlchemy()       # ORM for database models
migrate = Migrate()     # Database migrations
jwt = JWTManager()      #