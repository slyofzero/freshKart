from flask import *
from config import Config
from routes import (
    categories_bp,
    auth_bp,
    category_bp,
    product_bp,
    cart_bp,
    order_bp,
    search_bp,
)
from datetime import timedelta
from models import db, Category, ProductRateTypes, Cart
from controllers.home import home_get_controller


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI

# Setting up user session params
app.secret_key = Config.SECRET_KEY
app.permanent_session_lifetime = timedelta(days=30)


# Initiating app for SQLAlchemy and creating database
with app.app_context():
    db.init_app(app=app)


# Shared variables
@app.context_processor
def inject_variable():
    user_is_logged_in = "id" in session
    user_is_admin = False
    categories_list = Category.query.order_by(Category.name.asc()).all()
    rates_list = [rate_type for rate_type in ProductRateTypes]

    if "role" in session and session["role"] == "ADMIN":
        user_is_admin = True

    return {
        "user_is_logged_in": user_is_logged_in,
        "user_is_admin": user_is_admin,
        "categories_list": categories_list,
        "session": session,
        "rates_list": rates_list,
    }


# App routes
@app.route("/")
def index():
    return home_get_controller()


app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(categories_bp, url_prefix="/categories")
app.register_blueprint(category_bp, url_prefix="/category")
app.register_blueprint(product_bp, url_prefix="/product")
app.register_blueprint(cart_bp, url_prefix="/cart")
app.register_blueprint(order_bp, url_prefix="/orders")
app.register_blueprint(search_bp, url_prefix="/search")

# Only run the app when this file is executed
if __name__ == "__main__":
    app.run(debug=True)
