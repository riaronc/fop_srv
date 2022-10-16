from app import db
from app.models import Fop


class FopDAO:

    @staticmethod
    def get_all() -> list[Fop]:
        fops = db.session.query(Fop)
        return fops

    @staticmethod
    def create(data: dict):
        fop = Fop(**data)
        db.session.add(fop)
        db.session.commit()
        return fop

    @staticmethod
    def get_selected_fop(id: int) -> Fop:
        fop = Fop.query.get(id)
        if not fop:
            raise ValueError("Fop not found")
        return fop

    @staticmethod
    def edit_selected(id: int, data: dict):
        fop = FopDAO.get_selected_fop(id=id)
        for k, v in data.items():
            if hasattr(Fop, k) and v is not None:
                setattr(fop, k, v)

        db.session.commit()
        return fop

    @staticmethod
    def delete(id: int):
        intent = FopDAO.get_selected_fop(id=id)
        intent.status = 'deleted'
        db.session.commit()
        return True


fop_dao = FopDAO()
