from flask import Blueprint, jsonify, request
from src.services.courseservice.course import CourseService
from flask_jwt_extended import jwt_required
from src.utility.role_decorator import roles_required

course_bp = Blueprint('courses', __name__)
course_service = CourseService()

@course_bp.route('/', methods=['Post'])
@roles_required("admin")
def create_course():
    try:
        data = request.get_json()
        course_service.create_course(data)
        return data,201
    except Exception as e:
        return jsonify({"error":str(e)}),400


@course_bp.route('/', methods=['Get'])
@roles_required("learner")
def get_all_courses():
    try:
        courses = course_service.get_all_courses()
        return jsonify(courses)
    except Exception as e:
        return jsonify({"error":str(e)}),400


@course_bp.route('/<int:id>', methods=['Get'])
@roles_required("instructor")
def get_course_by_course_id(id):
    try:
        course = course_service.get_course_by_id(id)
        return jsonify(course),200
    except Exception as e:
        return jsonify({"error":str(e)}),400

@course_bp.route('/<int:id>', methods=['Get'])
@roles_required(["instructor"])
def get_courses_by_user_id(id):
    try:
        course = course_service.get_course_by_id(id)
        return jsonify(course),200
    except Exception as e:
        return jsonify({"error":str(e)}),400

        