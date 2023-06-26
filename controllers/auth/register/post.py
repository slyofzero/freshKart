from flask import redirect


def register_post_controller(request):
    body = request.form.to_dict(flat=False)

    return redirect("/auth/register")
