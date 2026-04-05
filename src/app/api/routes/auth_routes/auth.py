from flask import Blueprint, jsonify, request
#from authlib.integrations.flask_client import OAuth
from src.services.authservice.auth import AuthService
from flask_jwt_extended import jwt_required
from flask_jwt_extended import unset_jwt_cookies

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/signup', methods=['Post'])
def signup():
    try:
        data = request.get_json()
        response = auth_service.signup(data)
        return response
    except Exception as e:
        return jsonify({"error":str(e)}),400
    
@auth_bp.route('/login', methods=['Post'])
def login():
    try:
        data = request.get_json()
        response = auth_service.login(data)
        return response
    except Exception as e:
        return jsonify({"error":str(e)}),400
    
@auth_bp.route('/refresh', methods=['POST'])
@jwt_required
def refresh():
    try:
        resp = auth_service.refresh()
        return resp
    except Exception as e:
        return jsonify({"error": str(e)}),400 

@auth_bp.route('/logout', methods=['POST'])
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200

@auth_bp.route('/login_user', methods=['POST'])
@jwt_required("admin")
def get_current_user():
    try:
        response = auth_service.get_current_user()
        return response
    except Exception as e:
        return jsonify({"error":str(e)}),400