from flask import *
from config import Config
from routes import category_bp, auth_bp

from models import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI


# Initiating app for SQLAlchemy and creating database
with app.app_context():
    db.init_app(app=app)


# App routes
@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(category_bp, url_prefix="/<category>")

# Only run the app when this file is executed
if __name__ == "__main__":
    app.run(debug=True)
