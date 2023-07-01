from flask import Blueprint, request
from controllers.cart import (
    cart_get_controller,
    cart_post_controller,
    cart_update_controller,
    cart_delete_controller,
)
from controllers.buy import buy_controller, buy_all_controller

cart_bp = Blueprint(
    "cart_bp", __name__, static_folder="static", template_folder="template"
)


@cart_bp.route("/", methods=["GET"])
def get_cart():
    return cart_get_controller(request=request)


@cart_bp.route("/", methods=["POST"])
def post_cart():
    return cart_post_controller(request=request)


@cart_bp.route("/buy-all", methods=["POST"])
def buy_all():
    return buy_all_controller(request=request)


@cart_bp.route("/update/<cart_id>", methods=["POST"])
def update_cart(cart_id):
    return cart_update_controller(cart_id=cart_id, request=request)


@cart_bp.route("/delete/<cart_id>", methods=["POST"])
def delete_cart(cart_id):
    return cart_delete_controller(cart_id=cart_id, request=request)


@cart_bp.route("/buy/<cart_id>", methods=["POST"])
def buy(cart_id):
    return buy_controller(cart_id=cart_id, request=request)
