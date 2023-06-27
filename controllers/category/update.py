from flask import redirect, session
from models import db, Category


def category_update_controller(category, request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new category")

        body = request.form.to_dict(flat=True)
        new_category_name = body["name"]

        category = Category.query.filter_by(name=category).first()

        if category:
            category.name = new_category_name
            db.session.commit()

        return redirect("/categories")

    except Exception as error:
        return redirect("/")
