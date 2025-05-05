from werkzeug.security import generate_password_hash
from ..extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Colum(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    prefix = db.Column(db.String(10))
    phone_number = db.Column(db.String(50), unique=True, index=True)
    date_of_birth = db.Column(db.String(10))
    address = db.Column(db.Text)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(10))
    country = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)

    accounts = db.relationship("Account", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
