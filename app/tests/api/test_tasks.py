from .utils import api_request
from http import HTTPMethod


def test_create_task():
    # requests.delete("http://127.0.0.1:8000/tasks/")
    api_request(method=HTTPMethod.DELETE, endpoint="/tasks/", expected_status=200)

    # created_task = requests.post(
    #     url="http://127.0.0.1:8000/tasks/", json={"description": "string"}
    # )

    created_task = api_request(
        method=HTTPMethod.POST, endpoint="/tasks", json={"description": "string"}
    )
    assert created_task == {"id": 1, "description": "string", "completed": False}
