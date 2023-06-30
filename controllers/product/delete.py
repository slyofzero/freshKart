from flask import redirect, session
from models import db, Product, Category
import os
from config import root_dir


def product_delete_controller(product_id, request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new product")

        product = Product.query.filter_by(id=product_id).first()
        category = Category.query.filter_by(id=product.category).first()
        image = f"{root_dir}{product.image}"

        os.remove(image)

        if product:
            db.session.delete(product)
            db.session.commit()

        return redirect(f"/category/{category.name}")

    except Exception as error:
        print(error)
        return redirect("/")
