from app import db
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, password={self.password!r})"