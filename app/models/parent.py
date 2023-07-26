from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base
from pydantic import BaseModel
from typing import Optional, List
from app.models.child import ChildSchema, Child


class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)

    children = relationship(Child, back_populates="parent")


class ParentSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    children: List[ChildSchema] = None

    class Config:
        orm_mode = True
