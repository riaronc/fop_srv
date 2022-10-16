from app import db
from app.models import Task


class TaskDAO:

    @staticmethod
    def get_all() -> list[Task]:
        tasks = db.session.query(Task)
        return tasks

    @staticmethod
    def create(data: dict):
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_selected_task(id: int) -> Task:
        task = Task.query.get(id)
        if not task:
            raise ValueError("Task not found")
        return task

    @staticmethod
    def edit_selected(id: int, data: dict):
        task = TaskDAO.get_selected_task(id=id)
        for k, v in data.items():
            if hasattr(Task, k) and v is not None:
                setattr(task, k, v)

        db.session.commit()
        return task

    @staticmethod
    def delete(id: int):
        task = TaskDAO.get_selected_task(id=id)
        task.status = 'deleted'
        db.session.commit()
        return True


task_dao = TaskDAO()
