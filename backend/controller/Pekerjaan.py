from ..config.database import db_session
from ..models.model import Pekerjaan
from ..models.model import Pekerja
from sqlalchemy.orm import joinedload


def get_all():
    pekerjaan = db_session.query(Pekerjaan).options(
        joinedload(Pekerjaan.pekerja).options(joinedload(Pekerja.tipe_pekerja)),
        joinedload(Pekerjaan.pemberi_tugas).options(joinedload(Pekerja.tipe_pekerja))
    ).all()
    return {"content": [i.to_dict() for i in pekerjaan]}

def get_by_id(id:int):
    
    pekerjaan = db_session.query(Pekerjaan).filter_by(id=id).first()
    return {"content": pekerjaan.to_dict() }

def get_by_nama(nama:str):
    pekerjaan = db_session.query(Pekerjaan).filter_by(nama=nama).first()
    return {"content": pekerjaan.to_dict()}

def add(nama:str,pekerja_id:int,pemberi_tugas_id:int):
    pekerjaan = Pekerjaan(nama=nama, pekerja_id=pekerja_id, pemberi_tugas_id=pemberi_tugas_id, status="revisi")
    db_session.add(pekerjaan)
    db_session.commit()
    db_session.flush()
    db_session.refresh(pekerjaan)
    return {"content": pekerjaan.to_dict()}

def update_by_id(target_id,deskripsi_pekerjaan,status="revisi"):
    pekerjaan = db_session.query(Pekerjaan).filter_by(id=target_id)
    pekerjaan.update(
        {Pekerjaan.nama:deskripsi_pekerjaan}
        
    )    
    db_session.commit()
    db_session.flush()
    data = db_session.query(Pekerjaan).filter_by(id=target_id).first()
    return {"content": data.to_dict()}



