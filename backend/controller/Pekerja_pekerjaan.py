from ..config.database import db_session
from ..models.model import PekerjaPekerjaan 
from . import Pekerjaan as PekerjaanController
from . import Pekerja as PekerjaController
from . import Status as StatusController
from . import Aset as AsetController
from flask import jsonify
import json
from sqlalchemy.orm import joinedload
from datetime import datetime

def get_all():

    Pekerja_Pekerjaan = db_session.query(PekerjaPekerjaan).all()
    new_pekerjaan_list =[]
    for data in Pekerja_Pekerjaan:
        pekerja =  PekerjaController.get_by_id(data.pekerja_id)["content"]
        pekerjaan = PekerjaanController.get_by_id(data.pekerjaan_id)["content"]
        status_pekerjaan = StatusController.get_by_pekerjaan_id(data.pekerjaan_id)["content"]
        asset = AsetController.get_all_by_pekerjaan_id(data.pekerjaan_id)["content"]
        data_json = {
            "PekerjaanPekerja":data.to_dict(),
            "Pekerja":pekerja,
            "Pekerjaan":pekerjaan,
            "StatusPekerjaan":status_pekerjaan,
            "Aset":asset
        }
        new_pekerjaan_list.append(data_json)
        
    return{"content": new_pekerjaan_list}

def get_all_by_pekerjaan_id(pekerjaan_id:int):

    Pekerja_Pekerjaan = db_session.query(PekerjaPekerjaan).filter_by(pekerjaan_id=pekerjaan_id).all()
    new_pekerjaan_list =[]
    for data in Pekerja_Pekerjaan:
        pekerja =  PekerjaController.get_by_id(data.pekerja_id)["content"]
        pekerjaan = PekerjaanController.get_by_id(data.pekerjaan_id)["content"]
        status_pekerjaan = StatusController.get_by_pekerjaan_id(data.pekerjaan_id)["content"]
        asset = AsetController.get_all_by_pekerjaan_id(data.pekerjaan_id)["content"]
        data_json = {
            "PekerjaanPekerja":data.to_dict(),
            "Pekerja":pekerja,
            "Pekerjaan":pekerjaan,
            "StatusPekerjaan":status_pekerjaan,
            "Aset":asset
        }
        new_pekerjaan_list.append(data_json)
        
    return{"content": new_pekerjaan_list}

def add(nama_pekerjaan,pekerja_id,pekerjaan_id,position,type_status,path_file,due_date):
    
    pekerjaan = PekerjaanController.add(nama_pekerjaan)["content"]
    status_pekerjaan = StatusController.add(pekerjaan["id"],datetime.now(),type_status,due_date)["content"]
    asset = AsetController.add(path_file,"DOKUMEN",pekerjaan["id"])["content"]

    pekerja_pekerjaan = PekerjaPekerjaan(pekerja_id=pekerja_id,pekerjaan_id=pekerjaan["id"],position=position)
    db_session.add(pekerja_pekerjaan)
    db_session.commit()
    db_session.flush()
    db_session.refresh(pekerja_pekerjaan)

    return {"content": {"PekerjaanPekerja":pekerja_pekerjaan.to_dict(),"Pekerjaan":pekerjaan,"StatusPekerjaan":status_pekerjaan,"Aset":asset}}

def delete_by_id (pekerjaan_id):
    pekerja_pekerjaan = db_session.query(PekerjaPekerjaan).filter_by(pekerjaan_id=pekerjaan_id)
    data=pekerja_pekerjaan.first()
    res = data.to_dict()
    pekerja_pekerjaan.delete()
    db_session.commit()
    db_session.flush()
    return {"content": res}

def update_by_pekerjaan(pekerjaan_id,nama_job,id_pekerja,id_reviewer,object_job,document_terkait):
    #update pekerjaan name
    Pekerjaan.update_by_nama(nama_job)
    #update pekerja
    pekerja_pekerjaan = db_session.query(PekerjaPekerjaan).filter_by(pekerjaan_id=pekerjaan_id,pekerja_id=id_pekerja)
    pekerja_pekerjaan.update(
        {Pekerja_Pekerjaan.pekerja_id:id_pekerja
        }
    )
    db_session.commit()
    db_session.flush()
    #update reviewer
    pekerja_pekerjaan = AsetController.update_review_by_pekerjaan_id(pekerjaan_id,reviewer)

    #Update aset (document)
    pekerja_pekerjaan = AsetController.update_doc_by_pekerjaan_id(pekerjaan_id,document_terkait)

    #Update reviewver
    pekerja_pekerjaan = db_session.query(PekerjaPekerjaan).filter_by(pekerjaan_id=pekerjaan_id,pekerja_id=id_reviewer)
    pekerja_pekerjaan.update(
        {Pekerja_Pekerjaan.pekerja_id:id_reviewer
        }
    )
    db_session.commit()
    db_session.flush()
    #returning result data after update
    data = db_session.query(PekerjaPekerjaan).filter_by(pekerjaan_id=pekerjaan_id).all()
    return{"content": data.to_dict()}
