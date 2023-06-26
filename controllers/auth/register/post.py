from flask import redirect, render_template
from models import db, User


def register_post_controller(request):
    body = request.form.to_dict(flat=True)
    fname, lname, email, password, confirmPassword = body.values()

    try:
        if password != confirmPassword:
            raise ValueError("Password must match")

        newest_user = User.query.order_by(User.created_at.desc()).first()

        new_user_id = None
        if newest_user:
            new_user_id = newest_user.id + 1
        else:
            new_user_id = 0

        new_user = User(
            id=new_user_id, fname=fname, lname=lname, email=email, password=password
        )
        new_user.set_password()
        db.session.add(new_user)
        db.session.commit()

        return redirect("/auth/login")
    except Exception as error:
        error_msg = str(error)

        if "UNIQUE constraint failed: user.email" in error_msg:
            error_msg = "Email ID already in use"

        return render_template("auth/register.html", error_msg=error_msg)
