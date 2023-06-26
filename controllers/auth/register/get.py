from flask import render_template, session, redirect


def register_get_controller(request):
    if "id" in session:
        return redirect("/")

    return render_template("auth/register.html")
