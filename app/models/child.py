from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    parent_id = Column(
        "parent_id",
        Integer(),
        ForeignKey("parents.id"),
        nullable=False,
    )

    parent = relationship("Parent", back_populates="children")


class ChildSchema(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True
