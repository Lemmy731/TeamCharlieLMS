import requests
from flask import Blueprint, jsonify, request,redirect,url_for
#from authlib.integrations.flask_client import OAuth
from src.services.authservice.auth import AuthService
from flask_jwt_extended import jwt_required
from flask_jwt_extended import unset_jwt_cookies
from src.utility.verify_reset_token import verify_reset_token
from src.utility.generate_reset_token import generate_reset_token
from flask_mail import Mail, Message
from src.app.extensions import mail

auth_bp = Blueprint('auth', __name__)
callback_auth_bp = Blueprint('callback', __name__)

auth_service = AuthService()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        response = auth_service.signup(data)
        return response
    except Exception as e:
        return jsonify({"error":str(e)}),400
    
@auth_bp.route('/login', methods=['POST'])
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

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    try:
        data = request.get_json()
        email = data['email']
        response = auth_service.forgot_password(email)
        if response == "no user found for this email":
            return jsonify({"message":response}),400
        token = generate_reset_token(response)
        reset_link = url_for('auth.reset_password', token=token, _external=True)
        msg = Message('Password Reset', sender='noreply@yopmail.com', recipients=[email])
        msg.body = f'Click the link to reset your password: {reset_link}'
        mail.send(msg)
        return({"message":"Password reset link has been sent to your email"}),200
    except Exception as e:
        return jsonify({"error": str(e), "data":token}),400 

@auth_bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    email = verify_reset_token(token)
    if not email:
        return ('Invalid or expired token', 'error')
    if request.method == 'POST':
        data = request.get_json()
        response = auth_service.reset_password(data['new_password'], data['confirm_password'], email)
        if response == "password updated successfully":
            return({"message":response}),200
        return({"message":response}),400
    
@auth_bp.route("/google/login")
def google_login():
    try:
        request_uri = auth_service.google_login()
        return redirect(request_uri)
    except Exception as e:
          return jsonify({"error": str(e)}),400 


@callback_auth_bp.route("/google/callback")
def google_callback():
    try:
        code = request.args.get("code")
        if not code:
            return jsonify({"error": "Authorization code not provided"}), 400
        response = auth_service.google_callback(code)
        return response
    except Exception as e:
          return jsonify({"error": str(e)}),400 


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_login_user():
    try:
        response = auth_service.get_current_user()
        return response
    except Exception as e:
        return jsonify({"error":str(e)}),400
    