from src.models.course import Course
from src.dataaccess.coursedataaccess.course import CourseData

class CourseService:
    def __init__(self):
        self.course_datalayer = CourseData()

    def create_course(self, data):
        new_course = Course(
            title = data['title'],
            price = data['price'],
            description = data['description'],
            image_thumbnail = data['image_thumbnail'],
            duration = data['duration'],
            lessons_count = data['lessons_count'],
            rating = data['rating'])
        response = self.course_datalayer.create_course(new_course)
        return response
    
    def get_all_courses(self):
        courses = self.course_datalayer.get_all_courses()
        if not courses:
            return None
        return [c.to_dict() for c in courses]
    
    def get_course_by_id(self, course_id):
        course = self.course_datalayer.get_course_by_id(course_id)
        if not course:
            return None
        return course.to_dict()
    
    def get_courses_by_user_id(self, user_id):
        course = self.course_datalayer.get_courses_by_user_id(user_id)
        if not course:
            return None
        return course.to_dict()
    
