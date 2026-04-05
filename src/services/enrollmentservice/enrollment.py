from src.models.enrollment import Enrollment
from src.dataaccess.enrollmentdataaccess.enrollment import EnrollData

class EnrollmentService:
    def __init__(self):
        self.enroll_data_layer = EnrollData()

    def enroll_user(self, data):
        response = self.enroll_data_layer.enroll(data)
        return response
