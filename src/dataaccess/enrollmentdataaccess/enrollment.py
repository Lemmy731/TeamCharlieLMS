from src.app.extensions import db
from src.models.enrollment import Enrollment

class EnrollData:

    def enroll(self, enrollment):
        db.session.add(enrollment)
        db.session.commit()
        return enrollment
    
    def get_enrollment(self, user_id, course_id):
        return Enrollment.query.filter_by(
            user_id = user_id,
            course_id = course_id
        ).first()

