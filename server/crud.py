from sqlalchemy.orm import Session

import models, schemas


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.Todo):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, id: int):
    db.query(models.Todo).filter(models.Todo.id == id).delete()
    db.commit()
    return


def update_todo(db: Session, id: int, data: dict):
    pass
