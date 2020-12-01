from ..config.database import db_session
from ..models.model import Status


def get_all():
    status = db_session.query(Status).all()
    return{"content": [i.to_dict() for i in status]}