from ..config.database import db_session
from ..models.model import TipePekerja

def get_all(): 
    
    tipe_pekerja = db_session.query(TipePekerja).all()
    return {"content": [i.to_dict() for i in tipe_pekerja]}

def get_by_id(id:int):
    
    tipe_pekerja = db_session.query(TipePekerja).filter_by(id=id).first()
    return {"content": tipe_pekerja.to_dict()}

def get_by_nama(nama:str):
    
    tipe_pekerja = db_session.query(TipePekerja).filter_by(nama=nama).first()
    return {"content": tipe_pekerja.to_dict()}


def add(nama:str):
    tipe_pekerja = TipePekerja(nama=nama) # variabel tipe_pekerja sama dengan TipePekerja yang dimana membutuhkan nama dari query
    db_session.add(tipe_pekerja) # menambah data session ke query TipePekerja
    db_session.commit() # menempatkan data session add pada antrian
    db_session.flush() # mengirim antrian
    db_session.refresh(tipe_pekerja) # ngingetin data session yang ilang karena terkirim ke query

    return {"content": tipe_pekerja.to_dict()}


def update_by_id(target_id,nama):
    tipe_pekerja = db_session.query(TipePekerja).filter_by(id=target_id)
    tipe_pekerja.update(
    { TipePekerja.nama:nama}
    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(TipePekerja).filter_by(id=target_id).first()
    return{"content": data.to_dict()}

def update_by_nama(target_nama,nama):
    tipe_pekerja = db_session.query(TipePekerja).filter_by(nama=target_nama)
    tipe_pekerja.update(
        {TipePekerja.nama:nama}
    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(TipePekerja).filter_by(nama=nama).first()
    return{"content": data.to_dict()}

def delete_by_id(target_id):
    tipe_pekerja = db_session.query(TipePekerja).filter_by(id=target_id)
    data=tipe_pekerja.first()
    tipe_pekerja.delete()
    db_session.commit()
    db_session.flush()
    return{"content": data.to_dict()}
