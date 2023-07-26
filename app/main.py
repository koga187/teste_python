from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app.models.base import Base
from app.models.parent import Parent, ParentSchema
from app.models.child import Child, ChildSchema

from typing import List


SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost/public"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/parents/", response_model=List[ParentSchema])
def get_parent(db: Session = Depends(get_db)):
    return db.query(Parent).order_by(Parent.id).all()


@app.post("/parents/", response_model=ParentSchema)
def post_parent(parent: ParentSchema, db: Session = Depends(get_db)):
    db_parent = Parent(**parent.dict())
    db.add(db_parent)

    db.commit()
    db.refresh(db_parent)

    for child in parent.children:
        db_children = Child(**child.dict())
        db.add(db_children)

    return ParentSchema.from_orm(db_parent)


@app.post("/child/", response_model=ChildSchema)
def post_child(child: ChildSchema, db: Session = Depends(get_db)):
    db_child = Child(**child.dict())
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return ChildSchema.from_orm(db_child)


@app.get("/child/", response_model=List[ChildSchema])
def get_child(db: Session = Depends(get_db)):
    return db.query(Child).order_by(Child.parent_id).all()
