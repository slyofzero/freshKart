from models import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.BLOB, nullable=False)
    manufacture_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime)
    rate = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    # Object representation
    def __repr__(self):
        return f"Product {self.id} created"
