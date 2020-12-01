from ..config.database import db_session
from ..models.model import Aset



def get_all():
    aset = db_session.query(Aset).all()
    return {"content": [i.to_dict() for i in aset]}


