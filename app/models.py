from .db import app, db
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    staff_no: Mapped[str] = mapped_column(ForeignKey("staff.staff_no"))
    user_name: Mapped[str] = mapped_column(String,unique=False, nullable=False)
    password: Mapped[str] = mapped_column(String,unique=False, nullable=False)

class Department(db.Model):
    department_id: Mapped[str] = mapped_column(String, primary_key=True, unique=True)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    dept_head: Mapped[str] = mapped_column(ForeignKey("staff.staff_no"))
    key_no: Mapped[str] = mapped_column(ForeignKey("key.key_no"))

class Staff(db.Model):
    staff_no: Mapped[str] = mapped_column(String, primary_key=True, unique=True)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    last_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    national_id_no: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    authorised: Mapped[str] = mapped_column(Boolean, unique=False, nullable=False, default=False)

class Key(db.Model):
    key_no: Mapped[str] = mapped_column(String, primary_key=True)
    available: Mapped[int] = mapped_column(Boolean, unique=False, nullable=False, default=True)


with app.app_context():
    db.create_all()