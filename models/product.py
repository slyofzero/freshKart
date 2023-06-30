from models import db, Enum
from datetime import datetime


class ProductRateTypes(Enum):
    RUPEES = "Rupees"  # standalone price
    RPL = "Rp/L"  # rupees per litre
    RPK = "Rp/Kg"  # rupees per kg
    RPG = "Rp/g"  # rupees per gram
    RPD = "Rp/doz"  # rupees per dozen


class ProductStatus(Enum):
    AVAILABLE = "AVAILABLE"
    RUNNING_OUT = "RUNNING_OUT"
    SOLD_OUT = "SOLD_OUT"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    manufacture_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Integer, default=0)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    rate = db.Column(db.Enum(ProductRateTypes), default=ProductRateTypes.RUPEES)
    category = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    status = db.Column(db.Enum(ProductStatus), default=ProductStatus.AVAILABLE)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    # Object representation
    def __repr__(self):
        return f"<Product {self.id}>"
