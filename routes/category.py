from flask import Blueprint, request, redirect
from routes import product_bp
from controllers.category import category_get_controller, category_delete_controller

category_bp = Blueprint(
    "category_bp", __name__, static_folder="static", template_folder="template"
)


# Route logic for /<category>
@category_bp.route("/")
def index():
    return redirect("/categories")


@category_bp.route("/<category>", methods=["GET"])
def category_name(category):
    return category_get_controller(category=category, request=request)


# # Route logic for /<category>/<product>
# category_bp.register_blueprint(product_bp, url_prefix="/<product>")


# Routes for deleting a category
@category_bp.route("/<category>/delete", methods=["POST"])
def delete_category(category):
    return category_delete_controller(category=category, request=request)
