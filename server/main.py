from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schemas
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todo/", response_model=schemas.Todo)
def create_todo(todo: schemas.Todo, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


@app.get("/todos", response_model=List[schemas.Todo])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    return todos


# TODO Route for deleting todos
