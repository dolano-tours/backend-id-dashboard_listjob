from ..config.database import db_session
from ..models.model import Pekerja

def get_all():
    
    pekerja = db_session.query(Pekerja).all()
    return {"content": [i.to_dict() for i in pekerja]}

def get_by_id(id:int):
    
    pekerja = db_session.query(Pekerja).filter_by(id=id).first()
    return {"content": pekerja.to_dict() }
def get_by_nama(nama:str):
    pekerja = db_session.query(Pekerja).filter_by(nama=nama).first()
    return {"content": pekerja.to_dict()}

def add(id_employee:int):
    pekerja = Pekerja(id_employee=id_employee,)
    db_session.add(pekerja)
    db_session.commit()
    db_session.flush()
    db_session.refresh(pekerja)
    return {"content": pekerja.to_dict()}


def delete_by_id (id_employee):
    pekerja = db_session.query(Pekerja).filter_by(id=id_employee)
    data=pekerja.first()
    pekerja.delete()
    db_session.commit()
    db_session.flush()
    return {"content": data.to_dict()}

def update_by_id(id,id_employee):
    pekerja = db_session.query(Pekerja).filter_by(id=id)
    pekerja.update(
        {Pekerja.id_employee:id_employee}
    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(Pekerja).filter_by(id=id).first()
    return {"content": data.to_dict()}

