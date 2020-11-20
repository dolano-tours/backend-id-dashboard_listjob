from ..config.database import db_session
from ..models.model import TipePekerja

def get_all():
    
    tipe_pekerja = db_session.query(TipePekerja).all()
    return {"content": [i.to_dict() for i in tipe_pekerja]}

def get_by_id(id:int):
    
    tipe_pekerja = db_session.query(TipePekerja).filter_by(id=id)
    return {"content": [i.to_dict() for i in tipe_pekerja]}
