from src.services.enrollmentservice.enrollment import EnrollmentService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

enroll_bp = Blueprint("enroll", __name__)
enroll_service = EnrollmentService()

@enroll_bp.route('/', methods=['Post'])
@jwt_required()
def Enroll():
    try:
        data = request.get_json()
        response = enroll_service.enroll_user(data)
        return jsonify(response),200
    except Exception as e:
        return ({"error": str(e)}),400
