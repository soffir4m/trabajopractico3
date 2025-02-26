from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Modelo de tarea
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Lista para almacenar tareas
tasks = []

# Ruta raíz
@app.get("/")
def read_root():
    return {
        "title": "FastAPI Trabajo Practico 3",
        "description": "Curso Mlops, Profesor Jorge Zapata, Estudiante Melany Ramirez ",
        "completed": False
    }

#ruta para obtener todas las tareas
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

#ruta para obtener una tarea por su índice
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

#crear una nueva tarea
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

#actualizar una tarea
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    return task

#eliminar una tarea
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks.pop(task_id)
    return {"message": f"Task '{deleted_task.title}' deleted successfully!"}
