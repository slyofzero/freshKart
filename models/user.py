from models import db, datetime, re, Enum, validates
from werkzeug.security import generate_password_hash, check_password_hash


# User table initializing
class UserRoles(Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class User(db.Model):
    # Table fields
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(UserRoles), default=UserRoles.USER.value)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    # Hashing user passwords
    def set_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, new_password):
        return check_password_hash(self.password, new_password)

    # Validating user's first and last name
    @validates("fname", "lname")
    def validate_name(self, key, name):
        # Checking if the field we are validating is correct
        if key == "fname":
            field_name = "First name"
        elif key == "lname":
            field_name = "Last name"
        else:
            raise ValueError("Invalid field")

        # Validating if the name has more than 2 characters and no numbers
        name_has_nums = bool(re.search(r"\d", name))

        if key == "fname" and len(name) < 2:
            raise ValueError(f"{field_name} needs to have atleast 2 characters")
        elif name_has_nums == True:
            raise ValueError(f"{field_name} cannot have digits in it")

        return name

    # Validating user's email-id
    @validates("email")
    def validate_email(self, key, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email):
            raise ValueError("Invalid email address")
        return email

    # Validing user's password
    @validates("password")
    def validate_password(self, key, password):
        if len(password) < 12:
            raise ValueError("Password must have atleast 12 characters")
        return password

    # Object representation
    def __repr__(self):
        return f"<User {self.id}>"
