from src.app.extensions import db
from src.models.user import User
from flask_bcrypt import Bcrypt
from flask import jsonify
from src.models.role import Role

bcrypt = Bcrypt()

class AuthData:

    def signup(self, data):
        email = data.email
        password = data.password
        if User.query.filter_by(email=email).first():
            return({"message":"user already exist"}),400
        hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
        data.password = hash_password

        learner_role = Role.query.filter_by(name="learner").first()
        if not learner_role:
            raise Exception("Role  not found.", learner_role)
        data.roles.append(learner_role)
        db.session.add(data)
        db.session.commit()
        return jsonify({"message":"user created"}),201
    
    def login(self, data):
        user = User.query.filter_by(email=data.email).first()
        if not user or not bcrypt.check_password_hash(user.password, data.password):
            return "invalid credential"
        return user
