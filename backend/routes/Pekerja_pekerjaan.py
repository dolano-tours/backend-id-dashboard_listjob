from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerja_pekerjaan
from flask_cors import cross_origin
import json
from ..controller.utils import upload_file

pekerja_pekerjaan_routes = Blueprint('Pekerja_pekerjaan', __name__)

@pekerja_pekerjaan_routes.route("/all", methods=['GET'])
@cross_origin()
def get_all():
    pekerja_pekerjaan = Pekerja_pekerjaan.get_all()
    return jsonify(pekerja_pekerjaan)

@pekerja_pekerjaan_routes.route("/all/<pekerjaan_id>", methods=['GET'])
@cross_origin()
def get_all_by_pekerjaan_id(pekerjaan_id:int):
    pekerja_pekerjaan = Pekerja_pekerjaan.get_all_by_pekerjaan_id(pekerjaan_id)
    return jsonify(pekerja_pekerjaan)

@pekerja_pekerjaan_routes.route("/add", methods=['POST'])#add sesuai dengan ID dan id employee yang ada dalam database Pekerja 
@cross_origin()
def add():
    pekerja_id = request.form.get('pekerja_id')
    pekerjaan_id = request.form.get('pekerjaan_id')
    position = request.form.get('position')
    nama = request.form.get('nama')
    type_status = request.form.get('status')
    due_date = request.form.get('due_date')
    path = request.files['file_path']
    path_file = upload_file(path)

    pekerja_pekerjaan = Pekerja_pekerjaan.add(nama,pekerja_id,pekerjaan_id,position,type_status,path_file,due_date)
    return jsonify(pekerja_pekerjaan)

@pekerja_pekerjaan_routes.route("/update", methods=['PUT'])
@cross_origin()
def update_by_id():
    id_pekerjaan = request.json.get('id_pekerjaan')
    nama_job = request.json.get('nama_job')
    nama_pekerja = request.json.get('id_pekerja')
    reviewer = request.json.get('id_reviewer')
    document_terkait = request.json.get('document_terkait')
    object_job = request.json.get('object_job')
    pekerja_pekerjaan = Pekerja_pekerjaan.update_by_id(id_pekerjaan,nama_job,id_pekerja,document_terkait,object_job,id_reviewer)
    return jsonify(pekerja)

@pekerja_pekerjaan_routes.route("/delete", methods=['POST'])
@cross_origin()
def delete_by_id(): 
    pekerjaan_id = request.json.get('pekerjaan_id')
    pekerja_pekerjaan = Pekerja_pekerjaan.delete_by_id(pekerjaan_id)
    return jsonify(pekerja_pekerjaan)
    

