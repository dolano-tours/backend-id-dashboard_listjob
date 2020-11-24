from flask import Blueprint, request, jsonify, Response
from ..controller import TipePekerja
import json

tipe_pekerja_routes = Blueprint('TipePekerja', __name__)

@tipe_pekerja_routes.route("/all", methods=['GET'])
def get_all():
    tipe_pekerja = TipePekerja.get_all()
    return jsonify(tipe_pekerja)

@tipe_pekerja_routes.route("/id/<id>", methods=['GET'])
def get_by_id(id:int):
    tipe_pekerja = TipePekerja.get_by_id(request.view_args["id"])
    return jsonify(tipe_pekerja)

@tipe_pekerja_routes.route("/nama/<nama>", methods=['GET'])
def get_by_nama(nama:str):
    tipe_pekerja = TipePekerja.get_by_nama(request.view_args["nama"])
    return jsonify(tipe_pekerja)

@tipe_pekerja_routes.route("/add", methods=['POST'])
def add():
    nama = request.json.get('nama')
    tipe_pekerja = TipePekerja.add(nama)

    return jsonify(tipe_pekerja)

@tipe_pekerja_routes.route("/update/id", methods=['PUT'])
def update_by_id():
    id  = request.json.get('id')
    nama = request.json.get('nama')
    tipe_pekerja = TipePekerja.update_by_id(id,nama)
    return jsonify(tipe_pekerja)

@tipe_pekerja_routes.route("/update/nama", methods=['PUT'])
def update_by_nama():
    target_nama = request.json.get('get_nama')
    nama = request.json.get('nama') 
    tipe_pekerja = TipePekerja.update_by_nama(target_nama,nama)
    return jsonify(tipe_pekerja)


@tipe_pekerja_routes.route("/delete", methods=['DELETE'])
def delete_by_id():
    id = request.json.get('id')
    tipe_pekerja = TipePekerja.delete_by_id(id)
    return jsonify(tipe_pekerja)