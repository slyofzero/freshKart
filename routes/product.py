from flask import Blueprint, request
from controllers.product import product_get_controller, product_post_controller

product_bp = Blueprint(
    "product_bp", __name__, static_folder="static", template_folder="template"
)


@product_bp.route("/", methods=["GET"])
def get_product():
    return product_get_controller(request=request)


@product_bp.route("/", methods=["POST"])
def post_product():
    return product_post_controller(request=request)
