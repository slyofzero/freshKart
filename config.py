import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URI = os.environ.get("DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")


root_dir = os.path.dirname(__file__)
