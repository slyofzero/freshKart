from flask import redirect, render_template
from models import Product, Category


def search_get_controller(request):
    try:
        products = Product.query.filter(Product.name.ilike(f"%%")).all()
        categories = Category.query.filter(Category.name.ilike(f"%%")).all()

        return render_template(
            "search.html", search="", products=products, categories=categories
        )
    except Exception as error:
        return redirect("/")
