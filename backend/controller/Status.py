from ..config.database import db_session
from ..models.model import Status


def get_all():
    status = db_session.query(Status).all()
    return{"content": [i.to_dict() for i in status]}

def get_by_id(id:int):
    status = db_session.query(Status).filter_by(id=id).first()
    return{"content": status.to_dict()}

def get_by_pekerjaan_id(id:int):
    status = db_session.query(Status).filter_by(pekerjaan_id=id).first()
    return{"content": status.to_dict()}

def add(pekerjaan_id,timestamp,typez,due_date):
    status = Status(pekerjaan_id=pekerjaan_id, timestamp=timestamp, type=typez,due_date=due_date)
    db_session.add(status)
    db_session.commit()
    db_session.flush()
    db_session.refresh(status)
    return {"content": status.to_dict()}
 
def delete_by_id(id):
     status = db_session.query(Status).filter_by(id=id)
     data=status.first()
     status.delete()
     db_session.commit()
     db_session.flush()
     return{"content": data.to_dict()}

def update_by_id(id,type):
    status = db_session.query(Status).filter_by(id=id)
    status.update(
        {Status.type:type}
    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(Status).filter_by(id=id).first()
    return{"content": data.to_dict()}