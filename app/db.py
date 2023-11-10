import os
from .app_init import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(app, model_class=Base)