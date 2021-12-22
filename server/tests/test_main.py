from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_todos():
    response = client.get("/todos/")
    print(response)
