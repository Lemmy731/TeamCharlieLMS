from src.dataaccess.roledataaccess.admin_assign_role import AssignRoleData

role_data = AssignRoleData()

class AssignRoleService:
    def assign_role(self, user_id, role):
        response = role_data.assign_role(user_id, role)
        return response
