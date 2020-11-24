from ..config.database import db_session
from ..models.model import Hasil

def get_all():
    
    hasil = db_session.query(Hasil).all()
    return {"content": [i.to_dict() for i in hasil]}

def get_by_id(id:int):
    
    hasil = db_session.query(Hasil).filter_by(id=id)
    return {"content": [i.to_dict() for i in hasil]}


def delete_by_id(target_id):
    hasil = db_session.query(hasil).filter_by(id=target_id)
    data = hasil.first()
    hasil.delete()
    db_session.commit()
    db_session.flush()
    return{"content": data.to_dict}

def add (pekerjaan_id:int,pekerja_id:int):
    hasil = Document(pekerja_id=pekerja_id, pekerjaan_id=pekerjaan_id)
    db_session.add(document)
    db_session.commit()
    db_session.flush()
    db_session.refresh(hasil)
    return {"content": hasil.to_dict()}

