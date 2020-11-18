from ..config.database import db_session
from ..models.model import TipePekerja

def get_all():
    tipe_pekerja = db_session.query(TipePekerja).all()
    return tipe_pekerja
