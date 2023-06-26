from flask import render_template


def product_get_controller(category, product, request):
    return render_template("product.html", product=product)
