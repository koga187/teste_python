from sqlalchemy.ext.declarative import as_declarative

# from sqlalchemy.sql import func
# from sqlalchemy import (
#     Column,
#     DateTime,
# )
from typing import Any


@as_declarative()
class Base:
    id: Any
    __name__: str

    # updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
