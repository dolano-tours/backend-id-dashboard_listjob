from ..config.database import db_session
from ..models.model import Aset



def get_all():
    aset = db_session.query(Aset).all()
    return {"content": [i.to_dict() for i in aset]}

def get_by_id(id:int):
    aset = db_session.query(Aset).filter_by(id=id).first()
    return {"content": aset.to_dict()}

def add(path_file:str, is_hasil:int, pekerjaan_id:int):
    aset = Aset(path_file=path_file, is_hasil=is_hasil, pekerjaan_id=pekerjaan_id)
    db_session.add(aset)
    db_session.commit()
    db_session.flush()
    db_session.refresh(aset)
    return{"content": aset.to_dict()}


def delete_by_id (id):
    aset = db_session.query(Aset).filter_by(id=id)
    data=aset.first()
    aset.delete()
    db_session.commit()
    db_session.flush()
    return{"content": data.to_dict()}

def update_by_id (id,path_file):
    aset = db_session.query(Aset).filter_by(id=id)#memfilter data dengan ID yang ada
    aset.update(
        {Aset.path_file:path_file}#yang akan di update adalah pathfilenya 

    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(Aset).filter_by(id=id).first()#filter data dengan ID dan paling awal muncul
    return{"content": data.to_dict()}

