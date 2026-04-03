from src.app.extensions  import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now)

    enrollments = db.relationship(
        "Enrollment",
        back_populates="course",
        lazy=True
    )

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "created_at":self.created_at
            }
        