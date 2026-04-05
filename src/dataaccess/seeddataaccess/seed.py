from src.models.role import Role
from src.app.extensions import db
from src.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class SeedData:
    def seed_role(self):
        roles = ["learner", "instructor", "admin"]
        for role in roles:
            if not Role.query.filter_by(name=role).first():
                db.session.add(Role(name=role))
                db.session.commit()
    print("Roles seeded successfully")

    def seed_admin(self):
        user = User(
            first_name = "admin",
            last_name = "admin",
            email = "admin@yopmail.com",
            password = "Admin@12345"
        )
        if User.query.filter_by(email=user.email).first():
            return("admin already exist")
        hash_password = bcrypt.generate_password_hash(user.password).decode('utf-8')
        user.password = hash_password
        admin_role = Role.query.filter_by(name="admin").first()
        if not admin_role:
            return "role not found"
        user.roles.append(admin_role)
        db.session.add(user)
        db.session.commit()



    
    