from src.utility.role_decorator import roles_required
from flask import request, Blueprint,jsonify
from src.services.roleservice.admin_assign_role import AssignRoleService

role_bp = Blueprint("role", __name__)
role_service = AssignRoleService()

@role_bp.route('/', methods=['Post'])
@roles_required("admin")
def assign_role():
    try:
        data = request.get_json()
        user_id = data["user_id"]
        role = data["role"]
        response = role_service.assign_role(user_id, role)
        return (response)
    except Exception as e:
        return ({"error": str(e)}),400

