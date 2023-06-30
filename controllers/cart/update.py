from flask import redirect, session
from models import db, Cart


def cart_update_controller(request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new cart")

        body = request.form.to_dict(flat=True)
        new_cart_name = body["name"]

        cart = Cart.query.filter_by(name=cart).first()

        if cart:
            cart.name = new_cart_name
            db.session.commit()

        return redirect("/categories")

    except Exception as error:
        return redirect("/")
