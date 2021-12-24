from sqlalchemy.orm import Session
from .models import Todo as sqlTodo
from .schemas import Todo


def get_all_todos(
    db: Session, skip: int = 0, limit: int = 100
) -> list[sqlTodo]:
    return db.query(sqlTodo).offset(skip).limit(limit).all()


def post_todo(db: Session, todo: Todo) -> sqlTodo:
    db_todo = sqlTodo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def remove_todo(db: Session, id: int) -> None:
    db.query(sqlTodo).filter(sqlTodo.id == id).delete()
    db.commit()
    return


def update_todo(db: Session, id: int, data: dict) -> None:
    db.query(sqlTodo).where(sqlTodo.id == id).update(data)
    db.commit()
    return
