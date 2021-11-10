from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    title: str
    text: str
    is_done: Optional[bool] = False

    class Config:
        orm_mode = True
