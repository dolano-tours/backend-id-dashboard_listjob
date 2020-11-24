from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerjaan
import json

pekerjaan_routes = Blueprint('Pekerjaan', __name__)

@pekerjaan_routes.route("/all", methods=['GET'])
def get_all():
    pekerjaan = Pekerjaan.get_all()
    return jsonify(pekerjaan)

@pekerjaan_routes.route("/id/<id>", methods=['GET'])
def get_by_id(id:int):
    pekerjaan = Pekerjaan.get_by_id(request.view_args["id"])
    return jsonify(pekerjaan)

@pekerjaan_routes.route("/nama/<nama>", methods=['GET'])
def get_by_nama(nama:str):
    pekerjaan=Pekerjaan.get_by_nama(request.view_args["nama"])
    return jsonify(pekerjaan)

@pekerjaan_routes.route("/add", methods=['POST'])
def add():
    nama = request.json.get('nama')
    pekerja_id = request.json.get('pekerja_id')
    pemberi_tugas_id = request.json.get('pemberi_tugas_id')
    pekerjaan = Pekerjaan.add(nama,pekerja_id,pemberi_tugas_id)
    return jsonify(pekerjaan)


@pekerjaan_routes.route("/update/id", methods=['POST'])
def update_by_id():
    target_id = request.json.get('get_id')
    deskripsi_pekerjaan = request.json.get('get_nama')

    pekerjaan = Pekerjaan.update_by_id(target_id, deskripsi_pekerjaan)
    return jsonify(pekerjaan)
    




    