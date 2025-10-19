from fastapi import FastAPI, HTTPException, status
from tasks import (
    get_all_tasks,
    get_completed_tasks,
    get_pending_tasks,
    get_task_by_id,
    get_tasks_count,
    add_task,
    delete_task,
    mark_task_completed,
    clear_all_tasks,
)
from fastapi.responses import RedirectResponse
from schemas import TaskCreate, TaskResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Task Manager API", version="1.0.0")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    return add_task(task.description)


@app.get("/tasks/", response_model=list[TaskResponse])
async def read_all_tasks():
    return get_all_tasks()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@app.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
async def complete_task(task_id: int):
    success = mark_task_completed(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return success


@app.delete("/tasks/{task_id}")
async def remove_task(task_id: int):
    success = delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Задача не найдена")


@app.get("/tasks/status/completed", response_model=list[TaskResponse])
async def read_completed_tasks():
    """Получить выполненные задачи"""
    return get_completed_tasks()


@app.get("/tasks/status/pending", response_model=list[TaskResponse])
async def read_pending_tasks():
    """Получить невыполненные задачи"""
    return get_pending_tasks()


@app.delete("/tasks/")
async def clear_tasks():
    """Очистить все задачи"""
    clear_all_tasks()
    return {"message": "Все задачи удалены"}


@app.get("/stats/")
async def get_stats():
    """Получить статистику по задачам"""
    total = get_tasks_count()
    completed = len(get_completed_tasks())
    pending = len(get_pending_tasks())

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_rate": round((completed / total * 100), 2) if total > 0 else 0,
    }
