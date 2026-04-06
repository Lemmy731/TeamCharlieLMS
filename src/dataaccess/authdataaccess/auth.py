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

    def google_callback(self, email,name):
        check_user = User.query.filter_by(email=email).first()
        if not check_user:
             user = User(
                  email=email,
                  first_name=name,
                  provider="google"
                  )
             learner_role = Role.query.filter_by(name="learner").first()
             if not learner_role:
                 raise Exception("Role  not found.")
             if learner_role not in user.roles:
                 user.roles.append(learner_role)
             db.session.add(user)
             db.session.commit()
             return user
        return check_user
    
    def get_current_user(self, user_id):
        user = User.query.get(int(user_id))
        if not user:
            return {"message": "User not found"}, 404
        return jsonify({
             "id": user.id,
            "email": user.email,
            "first_name":user.last_name,
            "roles": [role.name for role in user.roles]
        }), 200

    
