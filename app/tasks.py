tasks = []


def add_task(description: str):
    """Добавляет новую задачу в список"""
    if not description or not description.strip():
        raise ValueError("Описание задачи не может быть пустым")

    task_id = len(tasks) + 1
    task = {"id": task_id, "description": description.strip(), "completed": False}
    tasks.append(task)
    return task


def get_all_tasks():
    """Возвращает все задачи"""
    return tasks


def get_task_by_id(task_id):
    """Находит задачу по ID"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def mark_task_completed(task_id):
    """Отмечает задачу как выполненную"""
    task = get_task_by_id(task_id)
    if task:
        task["completed"] = True
        return task 
    return None


def delete_task(task_id):
    """Удаляет задачу по ID"""
    task = get_task_by_id(task_id)
    if task:
        tasks.remove(task)
        return True
    return False


def get_completed_tasks():
    """Возвращает выполненные задачи"""
    return [task for task in tasks if task["completed"]]


def get_pending_tasks():
    """Возвращает невыполненные задачи"""
    return [task for task in tasks if not task["completed"]]


def clear_all_tasks():
    """Очищает весь список задач"""
    tasks.clear()


def update_task_description(task_id, new_description):
    """Обновляет описание задачи"""
    if not new_description or not new_description.strip():
        raise ValueError("Новое описание задачи не может быть пустым")

    task = get_task_by_id(task_id)
    if task:
        task["description"] = new_description.strip()
        return True
    return False


def get_tasks_count():
    """Возвращает общее количество задач"""
    return len(tasks)
