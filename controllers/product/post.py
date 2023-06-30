from flask import session, redirect
from models import Product, db, Category, ProductStatus, ProductRateTypes
from utils import to_datetime
import os


def product_post_controller(request):
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

        newest_product = Product.query.order_by(Product.id.desc()).first()
        product_category = Category.query.filter_by(id=category).first()

        image = request.files["image"]
        upload_dir = os.path.join("static", "product")

        # Create the upload directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)

        if image:
            filename = image.filename
            image_path = os.path.join(upload_dir, filename)
            image.save(image_path)

        if newest_product:
            new_product_id = newest_product.id + 1
        else:
            new_product_id = 0

        # Added a status for product on creation
        if stock == 0:
            status = ProductStatus.SOLD_OUT
        elif stock < 10:
            status = ProductStatus.RUNNING_OUT
        else:
            status = ProductStatus.AVAILABLE

        new_product = Product(
            id=new_product_id,
            name=name,
            description=description,
            image=f"/{image_path}",
            manufacture_date=to_datetime(manufacture_date),
            expiry_date=to_datetime(expiry_date),
            stock=int(stock),
            price=float(price),
            rate=rate,
            category=int(category),
            status=status,
        )
        db.session.add(new_product)
        db.session.commit()

        return redirect(f"/category/{product_category.name}")

    except Exception as error:
        print(error)
        return redirect("/")
