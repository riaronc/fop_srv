from flask import render_template

from app.dao.fop_dao import fop_dao


def get_all():
    result = fop_dao.get_all()
    return render_template()


def get_fop(id: int) -> str:
    result = fop_dao.get_selected_fop(id=id)
    return render_template()


def add_new_fop(data: dict) -> str:
    result = fop_dao.create(data=data)
    return render_template()


def edit_fop(id: int, data: dict) -> str:
    result = fop_dao.edit_selected(id=id, data=data)
    return render_template()


def delete_fop(id: int) -> str:
    result = fop_dao.delete(id=id)
    return render_template()
