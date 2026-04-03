from src.dataaccess.authdataaccess.auth import AuthData
from flask import jsonify
from src.models.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import (create_access_token,create_refresh_token,get_jwt_identity, set_access_cookies,set_refresh_cookies
)

class AuthService:
    def __init__(self):
        self.auth_data = AuthData()

    def signup(self, data):
        user = User(
        first_name = data['first_name'],
        last_name  = data['last_name'],
        email = data['email'],
        password = data['password']
    )
        response = self.auth_data.signup(user)
        return (response)
    
    def login(self, data):
        login_dto = User(
        email = data['email'],
        password = data['password']
    )
        response = self.auth_data.login(login_dto)
        if response != "invalid credential":
            access_token = create_access_token(identity=response.email)
            refresh_token = create_refresh_token(identity=response.email)
            resp = jsonify({'login': True})
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp, 200
        
    def refresh():
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        resp = jsonify({'refresh': True})
        set_access_cookies(resp, access_token)
        return resp, 200
    
   