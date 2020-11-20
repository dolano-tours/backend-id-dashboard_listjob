from ..config.database import db_session
from ..models.model import Hasil

def get_all():
    
    hasil = db_session.query(Hasil).all()
    return {"content": [i.to_dict() for i in hasil]}

def get_by_id(id:int):
    
    hasil = db_session.query(Hasil).filter_by(id=id)
    return {"content": [i.to_dict() for i in hasil]}
