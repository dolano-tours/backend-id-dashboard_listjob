from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerjaan
from flask_cors import cross_origin

import json

pekerjaan_routes = Blueprint('Pekerjaan', __name__)
@pekerjaan_routes.route("/all", methods=['GET'])
@cross_origin()
def get_all():
    pekerjaan = Pekerjaan.get_all()
    return jsonify(pekerjaan)
@pekerjaan_routes.route("/id/<id>", methods=['GET'])
@cross_origin()
def get_by_id(id:int):
    pekerjaan = Pekerjaan.get_by_id(request.view_args["id"])
    return jsonify(pekerjaan)
@pekerjaan_routes.route("/nama/<nama>", methods=['GET'])
@cross_origin()
def get_by_nama(nama:str):
    pekerjaan=Pekerjaan.get_by_nama(request.view_args["nama"])
    return jsonify(pekerjaan)
@pekerjaan_routes.route("/add", methods=['POST'])
@cross_origin()
def add():
    nama = request.json.get('nama')
    pekerjaan = Pekerjaan.add(nama)
    return jsonify(pekerjaan)

@pekerjaan_routes.route("/delete", methods=['POST'])
@cross_origin()
def delete_by_id():#mendelete dengan ID yang di perlukan
    id = request.json.get('id') # membuata parameter untuk mengakses ID 
    pekerjaan = Pekerjaan.delete_by_id(id) 
    return jsonify(pekerjaan)
    
@pekerjaan_routes.route("/update", methods=['PUT']) 
@cross_origin()
def update_by_id():#update dengan mencari ID yang diperlukan
    id = request.json.get('id') # untuk memanggil entitas yang ada di dict
    nama = request.json.get('nama') # memanggil entitas yang ada di dict
    pekerjaan = Pekerjaan.update_by_id(id,nama) 
    return jsonify(pekerjaan)



    