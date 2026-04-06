from src.app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    provider = db.Column(db.String(50), default="local")

    enrollments = db.relationship("Enrollment", backref="user", lazy=True)
    roles = db.relationship(
        'Role',
        secondary='user_roles',
        back_populates='users')

    def to_dict(self):
        return{
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            "created_at":self.created_at
        }