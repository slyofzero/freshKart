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
        cart_total_price = 0

        for cart_item in cart:
            cart_data = {
                "id": cart_item.id,
                "total_price": cart_item.total_price,
                "quantity": cart_item.quantity,
                "unit_type": cart_item.unit.value,
            }
            cart_total_price += cart_item.total_price

            product = Product.query.filter_by(id=cart_item.product_id).first()
            cart_data["product_name"] = product.name
            cart_data["product_id"] = product.id
            cart_data["product_stock"] = product.stock
            cart_data["product_price"] = product.price
            cart_data["product_rate"] = product.rate.value

            carts_list.append(cart_data)

        return render_template(
            "/cart.html", carts_list=carts_list, cart_total_price=cart_total_price
        )
    except Exception as error:
        error_msg = str(error)
        print(error_msg)
        return redirect("/categories")
