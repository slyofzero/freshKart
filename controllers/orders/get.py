from flask import redirect, session, render_template
from models import db, Order, Product


def order_get_controller(request):
    try:
        if "id" not in session:
            raise ValueError("Login to view order")

        orders = (
            Order.query.filter_by(user_id=session["id"])
            .order_by(Order.updated_at.desc())
            .all()
        )

        orders_list = []

        for order_item in orders:
            order_data = {
                "id": order_item.id,
                "total_price": order_item.total_price,
                "quantity": order_item.quantity,
                "unit_type": order_item.unit.value,
            }

            product = Product.query.filter_by(id=order_item.product_id).first()
            order_data["product_name"] = product.name
            order_data["product_id"] = product.id
            order_data["product_stock"] = product.stock
            order_data["product_price"] = product.price
            order_data["product_rate"] = product.rate.value

            orders_list.append(order_data)

        return render_template("/order.html", orders_list=orders_list)
    except Exception as error:
        error_msg = str(error)
        print(error_msg)
        return redirect("/categories")
