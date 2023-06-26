from flask import Blueprint, request
from controllers.product import product_get_controller

product_bp = Blueprint(
    "product_bp", __name__, static_folder="static", template_folder="template"
)


@product_bp.route("/")
def index(category, product):
    return product_get_controller(category=category, product=product, request=request)
