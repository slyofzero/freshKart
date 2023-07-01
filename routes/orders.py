from flask import Blueprint, request
from controllers.orders import order_get_controller

order_bp = Blueprint(
    "order_bp", __name__, static_folder="static", template_folder="template"
)


@order_bp.route("/", methods=["GET"])
def get_cart():
    return order_get_controller(request=request)
