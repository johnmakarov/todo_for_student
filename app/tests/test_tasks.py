from app.tasks import (
    get_task_by_id,
    add_task,
    mark_task_completed,
)


# PASSED
def test_return_none_if_id_not_found():
    result = get_task_by_id(999)
    assert result is None


def test_return_id_task():
    add_task("sdfsfdfdsdsf")
    result = get_task_by_id(1)
    assert result is not None
    assert result["id"] == 1
    assert result["completed"] == False
    assert result["description"] == "sdfsfdfdsdsf"


def test_if_task_completed():
    mock_task = [{"id": 1, "title": "Test", "completed": False}]
    result = mark_task_completed(1)
    assert result == 1
    assert mock_task[0]["completed"] is True
