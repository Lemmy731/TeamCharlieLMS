from src.dataaccess.authdataaccess.auth import AuthData
import requests
from flask import jsonify
from src.models.user import User
from config.config import Config
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
        password = data['password'],   
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
            roles = [role.name for role in response.roles]
            access_token = create_access_token(identity=str(response.id), additional_claims={"role":roles})
            refresh_token = create_refresh_token(identity=str(response.id), additional_claims={"role":roles})
            resp = jsonify({"login": True,}
                           )
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp, 200
        return "invalid credential"
        
    def google_login(self):
        google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]
        request_uri = (
        authorization_endpoint
        + "?response_type=code"
        + "&client_id=" + Config.GOOGLE_CLIENT_ID
        + "&redirect_uri=" + Config.GOOGLE_REDIRECT_URI
        + "&scope=openid email profile"
    )
        return request_uri

    def google_callback(self, code):
        google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
        token_endpoint = google_provider_cfg["token_endpoint"]
        token_response = requests.post(
            token_endpoint,
            data={
            "code": code,
            "client_id": Config.GOOGLE_CLIENT_ID,
            "client_secret": Config.GOOGLE_CLIENT_SECRET,
            "redirect_uri": Config.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
            },
            )
        token_json = token_response.json()
        if "access_token" not in token_json:
            return jsonify({"error": "Failed to get access token"}), 400
        access_token = token_json.get("access_token")
        userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
        userinfo_response = requests.get(userinfo_endpoint,headers={"Authorization": f"Bearer{access_token}"},)
        userinfo = userinfo_response.json()
        email = userinfo["email"]
        name = userinfo.get("name")
        response = self.auth_data.google_callback(email, name)
        if not response:
            return jsonify({"error": "User creation failed"}), 400
        roles = [role.name for role in response.roles]
        access_token = create_access_token(identity=str(response.id), additional_claims={"role":roles})
        refresh_token = create_refresh_token(identity=str(response.id), additional_claims={"role":roles})
        resp = jsonify({"login": True,
                        "user": { 
                            "id": response.id,
                            "email": response.email, 
                            "roles": roles
                            }})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        return resp
        
    def refresh(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        resp = jsonify({'refresh': True})
        set_access_cookies(resp, access_token)
        return resp, 200
    
    def get_current_user(self):
        user_id = get_jwt_identity()
        print("JWT Identity:", get_jwt_identity())
        if not user_id:
            return jsonify({"error": "Invalid or missing token"}), 401
        response = self.auth_data.get_current_user(user_id)
        return response
      