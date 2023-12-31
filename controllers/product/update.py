from flask import session, redirect
from models import Product, db, Category, ProductStatus, ProductRateTypes
from utils import to_datetime
import os


def product_update_controller(product_id, request):
    try:
        if session["role"] != "ADMIN":
            raise Exception(f"Only admins can create a new product")

        body = request.form.to_dict(flat=True)
        (
            name,
            description,
            category,
            manufacture_date,
            expiry_date,
            stock,
            price,
            rate,
        ) = body.values()
        stock = int(stock)
        rate = eval(rate)

        # Added a status for product on updation
        if stock == 0:
            status = ProductStatus.SOLD_OUT
        elif stock < 10:
            status = ProductStatus.RUNNING_OUT
        else:
            status = ProductStatus.AVAILABLE

        product = Product.query.filter_by(id=product_id).first()
        product_category = Category.query.filter_by(id=category).first()

        image = request.files["image"]
        upload_dir = os.path.join("static", "product")

        # Create the upload directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)

        if image:
            filename = image.filename
            image_path = os.path.join(upload_dir, filename)
            image.save(image_path)

        if product:
            product.name = name
            product.description = description
            product.image = f"/{image_path}"
            product.manufacture_date = to_datetime(manufacture_date)
            product.expiry_date = to_datetime(expiry_date)
            product.stock = int(stock)
            product.price = float(price)
            product.category = int(category)
            product.status = status
            product.rate = rate

            db.session.commit()

        return redirect(f"/category/{product_category.name}")

    except Exception as error:
        print(error)
        return redirect("/")
