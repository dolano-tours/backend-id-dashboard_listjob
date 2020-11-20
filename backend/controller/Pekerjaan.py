from ..config.database import db_session
from ..models.model import Pekerjaan

def get_all():
    
    pekerjaan = db_session.query(Pekerjaan).all()
    return {"content": [i.to_dict() for i in pekerjaan]}

def get_by_id(id:int):
    
    pekerjaan = db_session.query(Pekerjaan).filter_by(id=id)
    return {"content": [i.to_dict() for i in pekerjaan]}
