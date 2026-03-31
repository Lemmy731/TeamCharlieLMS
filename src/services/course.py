from src.models.course import Course
from src.dataaccess.course import CourseData

class CourseService:
    def __init__(self):
        self.course_datalayer = CourseData()

    def create_course(self, data):
        new_course = Course(
            name = data['name'],
            price = data['price'],
            description = data['description']
            )
        response = self.course_datalayer.create_course(new_course)
        return response
    
    def get_all_courses(self):
        courses = self.course_datalayer.get_all_courses()
        return [c.to_dict() for c in courses]
    
    def get_course_by_id(self, course_id):
        course = self.course_datalayer.get_course_by_id(course_id)
        return course.to_dict()
