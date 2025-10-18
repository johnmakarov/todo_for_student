from app.tasks import (
    get_task_by_id,
    mark_task_completed,
)
import pytest


@pytest.mark.skip("jsdfjjsdfsjfd")
def test_return_none_if_id_not_found():
    result = get_task_by_id(999)
    assert result is None


def test_get_task_by_id(add_new_task):
    result = get_task_by_id(1)
    assert result is not None
    assert result["id"] == add_new_task["id"]
    assert result["completed"] == add_new_task["completed"]
    assert result["description"] == add_new_task["description"]


@pytest.mark.skip("jsdfjjsdfsjfd")
def test_if_task_completed():
    mock_task = [{"id": 1, "title": "Test", "completed": False}]
    result = mark_task_completed(1)
    assert result == 1
    assert mock_task[0]["completed"] is True
