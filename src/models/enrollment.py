from src.app.extensions import db
from datetime import datetime

class Enrollment(db.Model):
    __tablename__ = "enrollments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), db.ForeignKey("users.id"))
    course_id = db.Column(db.String(120), db.ForeignKey("courses.id"))
    created_at = db.Column(db.DateTime, default=datetime.now)

    course = db.relationship(
        "Course",
        back_populates="enrollments"
    )