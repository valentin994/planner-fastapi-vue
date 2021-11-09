from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    text: str
    is_done: bool

    class Config:
        orm_mode = True
