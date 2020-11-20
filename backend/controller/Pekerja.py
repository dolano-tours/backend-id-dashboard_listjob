from ..config.database import db_session
from ..models.model import Pekerja

def get_all():
    
    pekerja = db_session.query(Pekerja).all()
    return {"content": [i.to_dict() for i in pekerja]}