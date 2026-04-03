from src.app.extensions import db
from src.models.course import Course

class CourseData:

    def create_course(self, course):
        db.session.add(course)
        db.session.commit()
        return course
    
    def get_all_courses(self):
        return Course.query.all()
    
    def get_course_by_id(self, course_id):
        return Course.query.get(course_id)
    