from fastapi.testclient import TestClient
from ..database import Base
from ..main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_todo():
    response = client.post(
        "/todo/",
        json={"title": "test title", "text": "test text", "is_done": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "test title",
        "text": "test text",
        "is_done": False,
    }


def test_get_all_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == [
        {"title": "test title", "text": "test text", "id": 1, "is_done": False}
    ]


def test_delete_todo():
    response = client.delete("/todo/1")
    assert response.status_code == 200
    assert response.json() == "Deleted todo with id: 1"

# TODO Add more test
# TODO Separate tests into files for every route
