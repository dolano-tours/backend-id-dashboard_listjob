from flask import Blueprint, request, jsonify, Response
from ..controller import Aset
from ..controller import Pekerjaan
import json


Aset_routes = Blueprint('Aset', __name__)

@Aset_routes.route("/all", methods=['GET'])#view semua data
def get_all():
    aset = Aset.get_all()
    return jsonify(aset)

@Aset_routes.route('/id/<id>', methods=['GET'])#view By id data
def get_by_id(id:int):
    aset = Aset.get_by_id(request.view_args["id"])
    return jsonify(aset)

@Aset_routes.route("/add", methods=['POST'])
def add():
    path_file = request.json.get('path_file')
    is_hasil = request.json.get('is_hasil')
    pekerjaan_id = request.json.get('pekerjaan_id')#diharapkan bisa menyambung dengan controler pekerjaan untuk mengambil ID 
    aset = Aset.add(path_file, is_hasil, pekerjaan_id)
    return jsonify(aset)

@Aset_routes.route("/delete", methods=['POST'])#delete hanya dengan ID 
def delete_by_id():
    id = request.json.get('id')
    aset = Aset.delete_by_id(id)
    return jsonify(aset)

@Aset_routes.route("/update", methods=['PUT'])#mengupdate dengan memilih id
def update_by_id():
    id = request.json.get('id')
    path_file = request.json.get('path_file')
    aset = Aset.update_by_id(id,path_file)
    return jsonify(aset)