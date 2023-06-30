from flask import Blueprint, request
from controllers.cart import (
    cart_get_controller,
    cart_post_controller,
    cart_update_controller,
    cart_delete_controller,
)

cart_bp = Blueprint(
    "cart_bp", __name__, static_folder="static", template_folder="template"
)


@cart_bp.route("/", methods=["GET"])
def get_product():
    return cart_get_controller(request=request)


@cart_bp.route("/", methods=["POST"])
def post_product():
    return cart_post_controller(request=request)


@cart_bp.route("/update", methods=["POST"])
def update_product():
    return cart_update_controller(request=request)


@cart_bp.route("/delete", methods=["POST"])
def delete_product():
    return cart_delete_controller(request=request)
