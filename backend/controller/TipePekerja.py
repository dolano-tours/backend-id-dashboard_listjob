from ..config.database import db_session
from ..models.model import TipePekerja

def get_all():
    
    tipe_pekerja = db_session.query(TipePekerja).all()
    return {"content": [i.to_dict() for i in tipe_pekerja]}
