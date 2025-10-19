import pytest
from random import randint
from faker import Faker
import logging
import requests

fake = Faker()


@pytest.fixture()
def add_new_task_api():
    requests.delete(url="http://127.0.0.1:8000/tasks/")
    logging.info("Clear all tasks")
    task = requests.post(
        url="http://127.0.0.1:8000/tasks/",
        json={"description": f"{fake.name()} {randint(1, 100)}"},
    )
    logging.info(f"Create task by API: {task}")
    yield task.json()



