from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column()
    boards: Mapped[list["Board"]] = relationship(back_populates="owner")

class Board(Base):
    __tablename__ = "boards"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id")) 
    owner: Mapped["User"] = relationship(back_populates="boards")
    tasks: Mapped[list["Task"]] = relationship(back_populates="board") 

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column(default="todo")
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))
    
    board: Mapped["Board"] = relationship(back_populates="tasks")

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        onupdate=func.now()
    )