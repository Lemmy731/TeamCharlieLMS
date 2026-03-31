from src.models.enrollment import Enrollment
from src.dataaccess.enrollment import EnrollData

class EnrollmentService:
    def __init__(self):
        self.enroll_data_layer = EnrollData()

    def enroll_user(self, user_id, course_id):
        if self.enroll_data_layer.get_enrollment(user_id, course_id):
            return "user already enrolled"
        enrollment = Enrollment(
            user_id = user_id,
            course_id = course_id
        )
        response = self.enroll_data_layer.enroll(enrollment)
        return response