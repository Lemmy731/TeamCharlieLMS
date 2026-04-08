from src.services.enrollmentservice.enrollment import EnrollmentService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

enroll_bp = Blueprint("enroll", __name__)
enroll_service = EnrollmentService()

@enroll_bp.route('/', methods=['POST'])
@jwt_required()
def Enroll():
    try:
        data = request.get_json()
        response = enroll_service.enroll_user(data)
        return (response)
    except Exception as e:
        return ({"error": str(e)}),400

