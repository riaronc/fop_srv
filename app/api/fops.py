from flask import jsonify
from flask import request

from app.api import api_bp
from app.services import fop_service


@api_bp.route('/fops', methods=['GET'])
def get_all_fops():
    result = fop_service.get_all()
    return result


@api_bp.route('/fops/<int:id>', methods=['GET'])
def get_selected_fop(id: int):
    result = fop_service.get_fop(id=id)
    return result


@api_bp.route('/fops', methods=['POST'])
def post_fop():
    data = request.json
    result = fop_service.add_new_fop(data=data)
    return result


@api_bp.route('/fops/<int:id>', methods=['PUT'])
def edit_fop(id):
    data = request.json
    result = fop_service.edit_fop(id=id, data=data)
    return result


@api_bp.route('/fops/<int:id>', methods=['DELETE'])
def delete_image(id: int):
    result = fop_service.delete_fop(id=id)
    return result
