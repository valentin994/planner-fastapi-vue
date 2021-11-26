from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schemas
from typing import List

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/todos/", response_model=List[schemas.Todo])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    return todos


# TODO Route for deleting todos
# TODO Add pyproject toml
# TODO Tests & Coverage
