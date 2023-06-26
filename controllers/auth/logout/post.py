from flask import redirect, session


def logout_post_controller():
    if "id" in session:
        session.clear()

        return redirect("/auth/login")
