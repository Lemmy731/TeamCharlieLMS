from src.models.user import User
from src.models.role import Role
from src.app.extensions import db

class AssignRoleData:
    def assign_role(self, user_id, role):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        role = Role.query.filter_by(name=role).first()
        if not role:
            return {"message": "Role not found"}, 404
        if role in user.roles:
            return {"message": "User already has this role"}, 400
        user.roles.append(role)
        db.session.commit()
        return {"message": f"{role} role assigned successfully"}, 200
