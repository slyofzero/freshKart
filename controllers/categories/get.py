from flask import render_template
from models import Category


def categories_get_controller(request):
    categories = Category.query.order_by(Category.name.asc()).all()

    return render_template("categories.html", categories=categories)
