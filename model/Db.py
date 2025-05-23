from flask_sqlalchemy import SQLAlchemy

class Db():
    def __init__(self):
        self.db = SQLAlchemy()
        return self.db