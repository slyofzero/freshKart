from flask import redirect, session, render_template
from models import db, Cart, Product


def cart_get_controller(request):
    try:
        if "id" not in session:
            raise ValueError("Login to view cart")

        cart = (
            Cart.query.filter_by(user_id=session["id"])
            .order_by(Cart.updated_at.desc())
            .all()
        )

        carts_list = []

        for cart_item in cart:
            cart_data = {
                "id": cart_item.id,
                "quantity": cart_item.quantity,
                "total_price": cart_item.total_price,
                "quantity": cart_item.quantity,
                "unit_type": cart_item.unit_type,
            }

            product = Product.query.filter_by(id=cart_item.product_id).first()
            cart_data["product_name"] = product.name
            cart_data["product_stock"] = product.stock

            carts_list.append(cart_data)

        return render_template("/cart.html", carts_list=carts_list)
    except Exception as error:
        error_msg = str(error)
        return redirect("/auth/login")
