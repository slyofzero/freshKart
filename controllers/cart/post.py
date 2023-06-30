from flask import redirect, session
from models import db, Cart, Product, ProductRateTypes, UnitTypes


def cart_post_controller(request):
    try:
        if "id" not in session:
            raise ValueError("Login to view cart")

        body = request.form.to_dict(flat=True)
        id, quantity = body.values()
        quantity = int(quantity)

        newest_cart = Cart.query.order_by(Cart.id.desc()).first()
        product = Product.query.filter_by(id=id).first()
        product_rate = product.rate

        total_price = product.price * quantity

        # Setting cart ID
        if newest_cart:
            new_cart_id = newest_cart.id + 1
        else:
            new_cart_id = 0

        # Setting product units to add to cart
        if product_rate == ProductRateTypes.RUPEES:
            unit_type = UnitTypes.UNITS
        elif product_rate == ProductRateTypes.RPL:
            unit_type = UnitTypes.LITER
        elif product_rate == ProductRateTypes.RPK:
            unit_type = UnitTypes.KG
        elif product_rate == ProductRateTypes.RPG:
            unit_type = UnitTypes.G
        elif product_rate == ProductRateTypes.RPD:
            unit_type = UnitTypes.DOZEN
        else:
            unit_type = None

        new_cart = Cart(
            id=new_cart_id,
            user_id=session["id"],
            product_id=id,
            quantity=quantity,
            unit=unit_type,
            total_price=total_price,
        )
        db.session.add(new_cart)
        db.session.commit()

        return redirect("/cart")

    except Exception as error:
        print(error)
        return redirect("/")
