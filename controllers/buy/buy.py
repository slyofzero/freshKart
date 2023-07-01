from flask import redirect, session
from models import db, Cart, Product, Order


def buy_controller(cart_id, request):
    try:
        if "id" not in session:
            raise ValueError("Login to view cart")

        cart = Cart.query.filter_by(id=cart_id).first()
        newest_order = Order.query.order_by(Order.id.desc()).first()

        # Setting cart ID
        if newest_order:
            new_order_id = newest_order.id + 1
        else:
            new_order_id = 0

        if cart:
            product = Product.query.filter_by(id=cart.product_id).first()
            product.stock -= cart.quantity

            new_order = Order(
                id=new_order_id,
                user_id=session["id"],
                product_id=cart.product_id,
                quantity=cart.quantity,
                unit=cart.unit,
                total_price=cart.total_price,
            )

            db.session.add(new_order)
            db.session.delete(cart)
            db.session.commit()

        return redirect("/cart")

    except Exception as error:
        print(error)
        return redirect("/")
