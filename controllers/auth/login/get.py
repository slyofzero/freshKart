from flask import render_template, session, redirect


def login_get_controller(request):
    if "id" in session:
        return redirect("/")

    return render_template("auth/login.html")
