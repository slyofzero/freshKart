from flask import redirect, session
from models import db, Category


def category_delete_controller(category, request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new category")

        category = Category.query.filter_by(name=category).first()

        if category:
            db.session.delete(category)
            db.session.commit()

        return redirect("/categories")

    except Exception as error:
        return redirect("/")
