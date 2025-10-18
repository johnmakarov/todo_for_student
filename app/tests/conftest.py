import pytest
from random import randint
from faker import Faker
from app.tasks import add_task

fake = Faker()


@pytest.fixture()
def add_new_task():
    task = add_task(description=f"{fake.name()} {randint(1, 100)}")
    print(f"TASK: {task}")
    yield task
