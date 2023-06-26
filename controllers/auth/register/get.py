from flask import render_template


def register_get_controller(request):
    return render_template("auth/register.html")
