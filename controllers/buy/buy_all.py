from flask import redirect, session, render_template
from models import db, Cart, Product, Order
from sqlalchemy import func


def buy_all_controller(request):
    try:
        if "id" not in session:
            raise ValueError("Login to view cart")

        carts = (
            Cart.query.filter_by(user_id=session["id"])
            .group_by(Cart.product_id)
            .with_entities(
                Cart.product_id, func.sum(Cart.quantity).label("total_quantity")
            )
            .all()
        )

        buy_error = ""
        for product, quantity in carts:
            product = Product.query.filter_by(id=product).first()

            if quantity > product.stock:
                buy_error = "There are items in the cart belonging to the same product. Their total quantity exceeds the available stock. Please only buy one cart item for now and wait for restocking of the product."

        if buy_error:
            return render_template("/cart.html", buy_error=buy_error)

        # Actual stuff here
        carts = Cart.query.filter_by(user_id=session["id"]).all()

        if len(carts) > 0:
            for cart in carts:
                newest_order = Order.query.order_by(Order.id.desc()).first()
                # Setting cart ID
                if newest_order:
                    new_order_id = newest_order.id + 1
                else:
                    new_order_id = 0

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
