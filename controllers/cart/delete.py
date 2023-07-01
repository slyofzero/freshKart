from flask import redirect, session
from models import db, Cart


def cart_delete_controller(cart_id, request):
    try:
        if "id" not in session:
            raise ValueError("Login to view cart")

        cart = Cart.query.filter_by(id=cart_id).first()

        if cart:
            db.session.delete(cart)
            db.session.commit()

        return redirect("/cart")

    except Exception as error:
        print(error)
        return redirect("/")
