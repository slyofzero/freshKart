import os
from dotenv import load_dotenv

load_dotenv()
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DATABASE_URI = os.environ.get("DATABASE_URI")
