from flask import redirect

from models import User


def login_post_controller(request):
    body = request.form.to_dict(flat=True)
    print(body)

    return redirect("/auth/login")
