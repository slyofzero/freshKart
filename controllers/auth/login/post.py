from flask import redirect


def login_post_controller(request):
    body = request.form.to_dict(flat=False)

    return redirect("/auth/login")
