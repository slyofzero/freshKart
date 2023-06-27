from flask import Blueprint, request
from controllers.categories import categories_get_controller, categories_post_controller

categories_bp = Blueprint(
    "categories_bp", __name__, static_folder="static", template_folder="template"
)


# Route logic for /<category>
@categories_bp.route("/", methods=["GET", "POST"])
def index():
    method = request.method

    if method == "GET":
        return categories_get_controller(request=request)

    elif method == "POST":
        return categories_post_controller(request=request)
