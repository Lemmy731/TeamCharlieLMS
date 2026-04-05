from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt

def roles_required(*required_roles):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            claims = get_jwt()

            user_roles = claims.get("role", [])  
            if isinstance(user_roles, str):
                user_roles = [user_roles]
            if not any(role in user_roles for role in required_roles):
                return jsonify({
                    "msg": "Access forbidden"
                }), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper