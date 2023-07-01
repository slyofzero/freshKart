from flask import redirect, render_template
from models import Product, Category


def search_post_controller(request):
    try:
        body = request.form.to_dict(flat=True)
        search = body["search"]

        products = Product.query.filter(Product.name.ilike(f"%{search}%")).all()
        categories = Category.query.filter(Category.name.ilike(f"%{search}%")).all()

        return render_template(
            "search.html", search=search, products=products, categories=categories
        )
    except Exception as error:
        print(error)
        return redirect("/categories")
