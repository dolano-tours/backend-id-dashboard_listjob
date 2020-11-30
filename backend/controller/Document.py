from ..config.database import db_session
from ..models.model import Document

def get_all():
    
    document = db_session.query(Document).all()
    return {"content": [i.to_dict() for i in document]}


def get_by_id(id:int):
    
    document = db_session.query(Document).filter_by(id=id)
    return {"content": [i.to_dict() for i in document]}


def update_by_id(target_id:int):
    document = db_session.query(Document).filter_by(id=target_id)
    document.update(
        {Document.path_file}
    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(Document).filter_by(id=target_id).first()
    return{"console": data.to_dict()}


def add (pekerjaan_id:int,pekerja_id:int):
    document = Document(pekerja_id=pekerja_id, pekerjaan_id=pekerjaan_id)
    db_session.add(document)
    db_session.commit()
    db_session.flush()
    db_session.refresh(document)
    return {"content": document.to_dict()}


def delete_by_id(target_id):
    document = db_session.query(document).filter_by(id=target)
    data = document.first()
    document.delete()
    db_session.commit()
    db_session.flush()
    return{"content": data.to_dict}





