from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .crud import get_all_todos, post_todo, remove_todo, update_todo
from .models import Base
from .schemas import Todo

Base.metadata.create_all(bind=engine)

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


@app.post("/todo/", response_model=Todo)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    return post_todo(db, todo)


@app.get("/todos/")
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_all_todos(db, skip, limit)
    return todos


@app.delete("/todo/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    remove_todo(db, id)
    return f"Deleted todo with id: {id}"


@app.patch("/todo/{id}")
def patch_todo(id: int, data: dict, db: Session = Depends(get_db)):
    update_todo(db, id, data)
    return {"id": id, **data}


# TODO Add pyproject toml
# TODO Tests & Coverage
