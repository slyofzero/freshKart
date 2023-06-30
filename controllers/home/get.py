from flask import render_template
from models import Category, Product


def home_get_controller():
    categories = Category.query.order_by(Category.name.asc()).all()
    data = {}

    try:
        for category in categories:
            products = (
                Product.query.order_by(Product.updated_at.desc())
                .filter_by(category=category.id)
                .limit(4)
                .all()
            )

            data[category.name] = products

        return render_template("index.html", categories=data)
    except Exception as error:
        return render_template("/")
