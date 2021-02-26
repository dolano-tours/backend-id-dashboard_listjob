from flask import Blueprint, request, jsonify, Response
from ..controller import Aset
from ..controller import Pekerjaan
from flask_cors import cross_origin
import json
from ..controller.utils import upload_file

Aset_routes = Blueprint('Aset', __name__)# 

@Aset_routes.route("/all", methods=['GET'])#view semua data
@cross_origin()
def get_all():
    aset = Aset.get_all()
    return jsonify(aset)

@Aset_routes.route('/id/<id>', methods=['GET'])#view By id data
@cross_origin()
def get_by_id(id:int):
    aset = Aset.get_by_id(request.view_args["id"])
    return jsonify(aset)

@Aset_routes.route("/add", methods=['POST'])
@cross_origin()
def add():
    the_file = request.files['path_file']
    is_hasil = request.form.get('is_hasil')
    pekerjaan_id = request.form.get('pekerjaan_id')#diharapkan bisa menyambung dengan controler pekerjaan untuk mengambil ID 
    path_file = upload_file(the_file)
    aset = Aset.add(path_file, is_hasil, pekerjaan_id)
    return jsonify(aset)

@Aset_routes.route("/delete", methods=['POST'])#delete hanya dengan ID 
@cross_origin()
def delete_by_id():
    id = request.json.get('id')
    aset = Aset.delete_by_id(id)
    return jsonify(aset)

@Aset_routes.route("/update", methods=['PUT'])#mengupdate dengan memilih id
@cross_origin()
def update_by_id():
    id = request.json.get('id')
    path_file = request.json.get('path_file')
    aset = Aset.update_by_id(id,path_file)
    return jsonify(aset)

@Aset_routes.route("/update_hasil", methods=['PUT'])#mengupdate dengan memilih id
@cross_origin()
def update_hasil_by_id():
    pekerjaan_id = request.json.get('pekerjaan_id')
    the_file = request.json.get('file')
    path_file = upload_file(the_file)
    check_if_exist = Aset.get_hasil_by_pekerjaan_id(pekerjaan_id)
    if check_if_exist:
        aset = Aset.update_hasil_by_pekerjaan_id(pekerjaan_id,path_file)
    else:
        aset = Aset.add(path_file,"HASIL",pekerjaan_id)
    return jsonify(aset)