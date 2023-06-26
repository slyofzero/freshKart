from flask import render_template


def login_get_controller(request):
    return render_template("auth/login.html")
