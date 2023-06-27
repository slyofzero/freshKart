from models import db, Enum
from datetime import datetime


class ProductRateTypes(Enum):
    RUPEES = "RUPEES"  # standalone price
    RPL = "RPL"  # rupees per litre
    RPK = "RPK"  # rupees per kg
    RPG = "RPG"  # rupees per gram
    RPD = "RPD"  # rupees per gram


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.BLOB, nullable=False)
    manufacture_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Integer, default=0)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    rate = db.Column(db.Enum(ProductRateTypes), default=ProductRateTypes.RUPEES)
    category = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    # Object representation
    def __repr__(self):
        return f"<Product {self.id}>"
