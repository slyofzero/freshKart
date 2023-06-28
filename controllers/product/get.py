from flask import render_template


def product_get_controller(product_id, request):
    return render_template("product.html", product_id=product_id)
