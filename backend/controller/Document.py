from ..config.database import db_session
from ..models.model import Document

def get_all():
    
    document = db_session.query(Document).all()
    return {"content": [i.to_dict() for i in document]}