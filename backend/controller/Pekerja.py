from ..config.database import db_session
from ..models.model import Pekerja

def get_all():
    
    pekerja = db_session.query(Pekerja).all()
    return {"content": [i.to_dict() for i in pekerja]}

def get_by_id(id:int):
    
    pekerja = db_session.query(Pekerja).filter_by(id=id)
    return {"content": pekerja.to_dict() }

def add(id_employee:int, tipe_pekerja_id:int):
    pekerja = Pekerja(id_employee=id_employee, tipe_pekerja_id=tipe_pekerja_id)
    db_session.add(pekerja)
    db_session.commit()
    db_session.flush()
    db_session.refresh(pekerja)
    return {"content": pekerja.to_dict()}

def delete_by_id(target_id):
    pekerja = db_session.query(Pekerja).filter_by(id=target_id)
    data=pekerja.first()
    pekerja.delete()
    db_session.commit()
    db_session.flush()
    return {"content": data.to_dict()}



