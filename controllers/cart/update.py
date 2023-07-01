from flask import redirect, session
from models import db, Cart, Product


def cart_update_controller(cart_id, request):
    try:
        if "id" not in session:
            raise Exception(f"Login to view cart")

        body = request.form.to_dict(flat=True)
        new_cart_quantity = body["quantity"]

        cart = Cart.query.filter_by(id=cart_id).first()

        if cart:
            product = Product.query.filter_by(id=cart.product_id).first()
            new_total_price = product.price * int(new_cart_quantity)

            cart.quantity = new_cart_quantity
            cart.total_price = new_total_price
            db.session.commit()

        return redirect("/cart")

    except Exception as error:
        return redirect("/")
