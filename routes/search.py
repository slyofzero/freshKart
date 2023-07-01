from flask import Blueprint, request
from controllers.search import search_post_controller, search_get_controller

search_bp = Blueprint(
    "search_bp", __name__, static_folder="static", template_folder="template"
)


@search_bp.route("/", methods=["POST", "GET"])
def search():
    if request.method == "GET":
        return search_get_controller(request=request)
    elif request.method == "POST":
        return search_post_controller(request=request)
