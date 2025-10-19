import requests


def test_create_task():
    requests.delete("http://127.0.0.1:8000/tasks/")
    
    created_task = requests.post(
        "http://127.0.0.1:8000/tasks/", json={"description": "string"}
    )
    assert created_task.status_code == 201
    assert created_task.json() == {"id": 1, "description": "string", "completed": False}
