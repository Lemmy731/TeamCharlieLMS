from src.app.extensions import db
from src.models.enrollment import Enrollment
from src.models.course import Course
from flask_jwt_extended import get_jwt_identity

class EnrollData:

    def enroll(self, data):
        user_id = int(get_jwt_identity())
        course_id = data['course_id']
        exist = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
        if exist:
            return ({"message":"already enrolled in this program"}),400
        course = db.session.get(Course, course_id)
        if not course:
            return ({"message":"no course found"})
        enroll = Enrollment(
            course_id = data['course_id'],
            user_id = user_id,
            name = course.name,
            status = "InProgress"
            )
        db.session.add(enroll)
        db.session.commit()
        return({"message":"user enrolled"}),200
    
    def get_enrollment(self, user_id, course_id):
        return Enrollment.query.filter_by(
            user_id = user_id,
            course_id = course_id
        ).first()

