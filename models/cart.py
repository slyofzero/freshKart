from models import db, Enum
from datetime import datetime


class UnitTypes(Enum):
    UNITS = ""  # standalone price
    LITER = "Liters"  # rupees per litre
    KG = "KGs"  # rupees per kg
    G = "grams"  # rupees per gram
    DOZEN = "dozen"  # rupees per dozen


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.Enum(UnitTypes), default=UnitTypes.UNITS)
    total_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    # Object representation
    def __repr__(self):
        return f"<Cart for {self.user_id}>"
