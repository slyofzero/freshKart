from flask import redirect, session
from models import db, Category


def categories_post_controller(request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new category")

        body = request.form.to_dict(flat=True)
        name = body["name"]

        newest_category = Category.query.order_by(Category.id.desc()).first()

        new_category_id = None
        if newest_category:
            new_category_id = newest_category.id + 1
        else:
            new_category_id = 0

        new_category = Category(id=new_category_id, name=name)
        db.session.add(new_category)
        db.session.commit()

        return redirect("/categories")

    except Exception as error:
        return redirect("/")
