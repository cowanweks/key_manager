from .app_init import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cowanweks:ultimate@localhost:5432/key_man"

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(app, model_class=Base)