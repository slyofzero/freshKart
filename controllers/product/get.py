from flask import render_template


def product_get_controller(request):
    return render_template("product.html")
