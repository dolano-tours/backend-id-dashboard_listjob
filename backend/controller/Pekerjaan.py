from ..config.database import db_session
from ..models.model import Pekerjaan

def get_all():
    pekerjaan = db_session.query(Pekerjaan).all()
    return {"content": [i.to_dict() for i in pekerjaan]}

def get_by_id(id:int):
    pekerjaan = db_session.query(Pekerjaan).filter_by(id=id).first()
    return {"content": pekerjaan.to_dict()}

def get_by_nama(nama:str):
    pekerjaan = db_session.query(Pekerjaan).filter_by(nama=nama).first()
    return {"content": pekerjaan.to_dict()}

def add(nama:str):
    pekerjaan = Pekerjaan(nama=nama)
    db_session.add(pekerjaan)
    db_session.commit()
    db_session.flush()
    db_session.refresh(pekerjaan)
    return {"content": pekerjaan.to_dict()}

def delete_by_id (target_id):
    pekerjaan = db_session.query(Pekerjaan).filter_by(id=target_id)
    data=pekerjaan.first()
    pekerjaan.delete()
    db_session.commit()
    db_session.flush()
    return {"content": data.to_dict()}

def update_by_id(id,nama):
    pekerjaan = db_session.query(Pekerjaan).filter_by(id=id)
    pekerjaan.update(
        {Pekerjaan.nama:nama}

    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(Pekerjaan).filter_by(id=id).first()
    return {"content": data.to_dict()}

def update_by_id(target_name,nama):
    pekerjaan = db_session.query(Pekerjaan).filter_by(name=target_name)
    pekerjaan.update(
        {Pekerjaan.nama:nama}

    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(Pekerjaan).filter_by(id=id).first()
    return {"content": data.to_dict()}


