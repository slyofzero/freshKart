from flask import Blueprint, render_template, redirect, request
from controllers.auth import (
    login_get_controller,
    login_post_controller,
    register_get_controller,
    register_post_controller,
    logout_post_controller,
)

auth_bp = Blueprint(
    "auth_bp", __name__, static_folder="static", template_folder="templates"
)


# For the login form
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    method = request.method

    if method == "GET":
        return login_get_controller(request)

    elif method == "POST":
        return login_post_controller(request)


# For the register form
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    method = request.method

    if method == "GET":
        return register_get_controller(request)

    elif method == "POST":
        return register_post_controller(request)


# For logging out
@auth_bp.route("/logout", methods=["POST"])
def logout():
    return logout_post_controller()
