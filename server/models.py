from database import Base
from sqlalchemy import String, Column, Integer, Boolean


class Todo(Base):
    __tablename__ = "Todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    is_done = Column(Boolean, default=False)
