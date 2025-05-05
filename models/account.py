from ..extensions import db


class Account(db):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_number = db.Column(db.String(50), unique=True, nullable=False)
    account_type = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Numeric(15, 2), default=0.00)
    currency = db.Column(db.String(3), default="PLN")
    opened_at = db.Column(db.DateTime, default=db.utcnow)
    status = db.Column(db.String(20), default="active")
