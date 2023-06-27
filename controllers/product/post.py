from flask import render_template, session, redirect, request
from models import Product, db, Category
from PIL import Image
from utils import to_datetime


def product_post_controller(request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new product")

        body = request.form.to_dict(flat=True)
        (
            name,
            description,
            category,
            image,
            manufacture_date,
            expiry_date,
            stock,
            price,
            rate,
        ) = body.values()

        newest_product = Product.query.order_by(Product.id.desc()).first()
        product_category = Category.query.filter_by(id=category).first()

        new_product_id = None
        if newest_product:
            new_product_id = newest_product.id + 1
        else:
            new_product_id = 0

        image_data = ""
        with open("static/doggie.jpeg", "rb") as f:
            image_data = f.read()

        new_product = Product(
            id=new_product_id,
            name=name,
            description=description,
            image=image_data,
            manufacture_date=to_datetime(manufacture_date),
            expiry_date=to_datetime(expiry_date),
            stock=int(stock),
            price=float(price),
            rate=rate,
            category=int(category),
        )
        db.session.add(new_product)
        db.session.commit()

        # return redirect(f"/category/{new_product.id}")
        return redirect(f"/category/")

    except Exception as error:
        print(error)
        return redirect("/")
