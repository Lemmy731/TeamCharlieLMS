from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from src.services.course import CourseService

course_bp = Blueprint('courses', __name__)
course_service = CourseService()

@course_bp.route('/', methods=['Post'])
# @jwt_required()
def create_course():
    try:
        data = request.get_json()
        course_service.create_course(data)
        return data,201
    except Exception as e:
        return jsonify({"error":str(e)}),400

@course_bp.route('/', methods=['Get'])
def get_all_courses():
    try:
        courses = course_service.get_all_courses()
        return jsonify(courses)
    except Exception as e:
        return jsonify({"error":str(e)}),400
    
@course_bp.route('/<int:id>', methods=['Get'])
def get_course_by_id(id):
    try:
        course = course_service.get_course_by_id(id)
        return jsonify(course),200
    except Exception as e:
        return jsonify({"error":str(e)}),400

        