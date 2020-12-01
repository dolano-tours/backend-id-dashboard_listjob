from ..config.database import db_session
from ..models.model import PekerjaPekerjaan 



def get_all():

    Pekerja_Pekerjaan = db_session.query(PekerjaPekerjaan).all()
    return{"content": [i.to_dict() for i in Pekerja_Pekerjaan]}

def add(pekerja_id,pekerjaan_id,position):
    pekerja_pekerjaan = PekerjaPekerjaan(pekerja_id=pekerja_id,pekerjaan_id=pekerjaan_id,position=position)
    db_session.add(pekerja_pekerjaan)
    db_session.commit()
    db_session.flush()
    db_session.refresh(pekerja_pekerjaan)
    return {"content": pekerja_pekerjaan.to_dict()}

def delete_by_id (pekerjaan_id,pekerja_id,position):
    pekerja_pekerjaan = db_session.query(PekerjaPekerjaan).filter_by(pekerjaan_id=pekerjaan_id,pekerja_id=pekerja_id,position=position)
    data=pekerja_pekerjaan.first()
    pekerja_pekerjaan.delete()
    db_session.commit()
    db_session.flush()
    return {"content": data.to_dict()}

def update_by_position(pekerja_id,pekerjaan_id,position):
    pekerja_pekerjaan = db_session.query(PekerjaPekerjaan).filter_by(pekerja_id=pekerja_id)
    pekerja_pekerjaan.update(
        {PekerjaPekerjaan.position:position}
    )
    db_session.commit()
    db_session.flush()
    data = db_session.query(PekerjaPekerjaan).filter_by(pekerja_id=pekerja_id).first()
    return{"content": data.to_dict()}
