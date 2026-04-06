from flask import Flask
from src.app.extensions import db, migrate, jwt
from config.config import DevelopmentConfig, ProductionConfig
from src.app.api.routes.course_routes.course import course_bp
from src.app.api.routes.enroll_routes.enrollment import enroll_bp
from src.app.api.routes.auth_routes.auth import auth_bp, callback_auth_bp
from src.models import user, course, enrollment, role, user_role
from src.services.seedservice.seed import SeedService
from src.app.api.routes.role_routes.role import role_bp
import os

config_map={
    "development":DevelopmentConfig,
    "production":ProductionConfig
}
def create_app():
    app = Flask(__name__)
    env = os.getenv("APP_ENV", "development")
    app.config.from_object(config_map.get(env, DevelopmentConfig))
    db.init_app(app)
    migrate.init_app(app, db)
    user, course, enrollment, role, user_role
    jwt.init_app(app)
    # with app.app_context():
    #     seeder = SeedService()
        # seeder.seed_role()
        # seeder.seed_admin()

    #register routes
    app.register_blueprint(course_bp, url_prefix="/api/course")
    app.register_blueprint(enroll_bp, url_prefix="/api/enroll")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(callback_auth_bp, url_prefix="/auth")
    app.register_blueprint(role_bp, url_prefix="/api/role")
    return app