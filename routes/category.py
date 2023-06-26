from flask import Blueprint, request
from routes import product_bp
from controllers.category import category_get_controller

category_bp = Blueprint(
    "category_bp", __name__, static_folder="static", template_folder="template"
)


# Route logic for /<category>
@category_bp.route("/")
def index(category):
    method = request.method

    if method == "GET":
        return category_get_controller(category=category, request=request)


# Route logic for /<category>/<product>
category_bp.register_blueprint(product_bp, url_prefix="/<product>")
