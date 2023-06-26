import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URI = os.environ.get("DATABASE_URI")
