from src.models.role import Role
from src.app.extensions import db
from src.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class SeedData:

    def seed_role(self):
        roles = ["learner", "instructor", "admin"]

        for role_name in roles:
            existing_role = Role.query.filter_by(name=role_name).first()

            if not existing_role:
                db.session.add(Role(name=role_name))

        db.session.commit()
        print("Roles seeded successfully")

    def seed_admin(self):
        email = "admin@yopmail.com"

        # check if admin exists FIRST
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print("Admin already exists")
            return

        admin_role = Role.query.filter_by(name="admin").first()
        if not admin_role:
            print("Role not found")
            return

        hashed_password = bcrypt.generate_password_hash("Admin@12345").decode("utf-8")

        user = User(
            first_name="admin",
            last_name="admin",
            email=email,
            password=hashed_password
        )

        user.roles.append(admin_role)

        db.session.add(user)
        db.session.commit()

        print("Admin created successfully")