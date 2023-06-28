from flask import Blueprint, request
from controllers.product import (
    product_get_controller,
    product_post_controller,
    product_update_controller,
    product_delete_controller,
)

product_bp = Blueprint(
    "product_bp", __name__, static_folder="static", template_folder="template"
)


@product_bp.route("/<product_id>", methods=["GET"])
def get_product(product_id):
    return product_get_controller(product_id=product_id, request=request)


@product_bp.route("/", methods=["POST"])
def post_product():
    return product_post_controller(request=request)


@product_bp.route("/<product_id>/update", methods=["POST"])
def update_product(product_id):
    return product_update_controller(product_id=product_id, request=request)


@product_bp.route("/<product_id>/delete", methods=["POST"])
def delete_product(product_id):
    return product_delete_controller(product_id=product_id, request=request)
