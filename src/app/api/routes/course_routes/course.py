from flask import Blueprint, jsonify, request
from src.services.courseservice.course import CourseService
from flask_jwt_extended import jwt_required
from src.utility.role_decorator import roles_required
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
import uuid

app_bp = Blueprint('image', __name__)
course_bp = Blueprint('courses', __name__)
course_service = CourseService()
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads", "courses")

@course_bp.route('/', methods=['POST'])
@roles_required("admin","instructor")
def create_course():
    try:
        data = request.form  
        image = request.files.get("image_thumbnail")
        image_path = None
        if image:
            filename = str(uuid.uuid4()) + "_" + secure_filename(image.filename)
            upload_folder = os.path.join(os.getcwd(), "uploads", "courses")
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
            image.save(file_path)
            image_path = f"/uploads/courses/{filename}"
        course_data = {
            "title": data.get("title"),
            "price": data.get("price"),
            "description": data.get("description"),
            "duration": data.get("duration"),
            "lessons_count": data.get("lessons_count"),
            "rating": data.get("rating", 0),
            "image_thumbnail": image_path
        }
        course = course_service.create_course(course_data)

        return jsonify({
            "message": "Course created successfully",
            "data": {
                "id": course.id,
                "title": course.title
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@course_bp.route('/', methods=['GET'])
@roles_required("admin","instructor","learner")
def get_all_courses():
    try:
        courses = course_service.get_all_courses()
        return jsonify(courses)
    except Exception as e:
        return jsonify({"error":str(e)}),400


@course_bp.route('/<int:id>', methods=['GET'])
@roles_required("admin","instructor")
def get_course_by_course_id(id):
    try:
        course = course_service.get_course_by_id(id)
        return jsonify(course),200
    except Exception as e:
        return jsonify({"error":str(e)}),400

@course_bp.route('/<int:id>', methods=['GET'])
@roles_required("instructor","admin")
def get_courses_by_user_id(id):
    try:
        course = course_service.get_course_by_id(id)
        return jsonify(course),200
    except Exception as e:
        return jsonify({"error":str(e)}),400

@app_bp.route("uploads/courses/<filename>")
def get_course_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
        