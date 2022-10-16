from flask import request

from app.api import api_bp
from app.services import tasks_service


@api_bp.route('/fops/<int:fop_id>/tasks', methods=['GET'])
def get_all_tasks():
    result = tasks_service.get_all()
    return result


@api_bp.route('/fops/<int:fop_id>/tasks/<int:task_id>', methods=['GET'])
def get_selected_fop(task_id: int):
    result = tasks_service.get_task(task_id=task_id)
    return result


@api_bp.route('/fops/<int:fop_id>/tasks', methods=['POST'])
def post_fop():
    data = request.json
    result = tasks_service.add_new_task(data=data)
    return result


@api_bp.route('/fops/<int:fop_id>/tasks/<int:task_id>', methods=['PUT'])
def edit_fop(task_id: int):
    data = request.json
    result = tasks_service.edit_task(task_id=task_id, data=data)
    return result


@api_bp.route('/fops/<int:fop_id>/tasks/<int:task_id>', methods=['DELETE'])
def delete_image(task_id: int):
    result = tasks_service.delete_task(id=task_id)
    return result
