from flask import render_template

from app.dao.task_dao import task_dao


def get_all():
    result = task_dao.get_all()
    return render_template()


def get_task(task_id: int) -> str:
    result = task_dao.get_selected_task(id=id)
    return render_template()


def add_new_task(data: dict) -> str:
    result = task_dao.create(data=data)
    return render_template()


def edit_task(id: int, data: dict) -> str:
    result = task_dao.edit_selected(id=id, data=data)
    return render_template()


def delete_task(id: int) -> str:
    result = task_dao.delete(id=id)
    return render_template()
