from flask import render_template
from models import Product, Category, ProductRateTypes


def category_get_controller(category, request):
    category = Category.query.filter_by(name=category).first()
    products = Product.query.filter_by(category=category.id).all()
    categories = Category.query.all()
    rates = [rate._value_ for rate in ProductRateTypes]

    return render_template(
        "category.html",
        category=category,
        products=products,
        categories=categories,
        rates=rates,
    )
