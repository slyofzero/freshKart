from flask import render_template
from models import Product, Category


def product_get_controller(product_id, request):
    product = Product.query.filter_by(id=product_id).first()
    category = Category.query.filter_by(id=product.category).first()

    return render_template("product.html", product=product, category=category)
