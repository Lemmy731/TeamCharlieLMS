from src.app.extensions  import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    image_thumbnail = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(120), nullable=True)
    duration = db.Column(db.Integer, nullable=False, default=0)
    lessons_count = db.Column(db.Integer, nullable=False, default=0)
    rating = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.now)

    enrollments = db.relationship(
        "Enrollment",
        back_populates="course",
        lazy=True
    )

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "price":self.price,
            "description":self.description,
            "created_at":self.created_at,
            "image_thumbnail":self.image_thumbnail,
            "duration":self.duration,
            "lessons_count":self.lessons_count,
            "rating":self.rating,
            }
        