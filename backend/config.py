from dotenv import getenv

class Config:
    """
    """

    def __init__(self):
        SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")