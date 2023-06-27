from flask import redirect, render_template, session
from models import User


def login_post_controller(request):
    body = request.form.to_dict(flat=True)
    email, password = body.values()

    try:
        user = User.query.filter_by(email=email).first()
        if user == None:
            raise ValueError(f"{email} not registered")

        password_matches = User.check_password(user, password)
        if password_matches == False:
            raise ValueError(f"Password doesn't match, please try again")

        session.update({"id": user.id, "email": email, "role": user.role.value})
        return redirect("/")

    except Exception as error:
        error_msg = str(error)

        return render_template("auth/login.html", error_msg=error_msg)
