from ..config.database import db_session
from ..models.model import Status


def get_all():
    status = db_session.query(Status).all()
    return{"content": [i.to_dict() for i in status]}

def get_by_id(id:int):
    status = db_session.query(Status).filter_by(id=id).first()
    return{"content": status.to_dict()}

def add(pekerjaan_id,timestamp,type):
    status = Status(pekerjaan_id=pekerjaan_id, timestamp=timestamp, type=type)
    db_session.add(status)
    db_session.commit()
    db_session.flush()
    db_session.refresh(status)
    return {"content": status.to_dict()}
