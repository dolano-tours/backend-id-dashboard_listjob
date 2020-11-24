from flask import Blueprint, request, jsonify, Response
from ..controller import Hasil
import json

hasil_routes = Blueprint('Hasil', __name__)

@hasil_routes.route("/all", methods=['GET'])
def get_all():
    hasil = Hasil.get_all()
    return jsonify(hasil)

@hasil_routes.route("/id/<id>", methods=['GET'])
def get_by_id(id:int):
    hasil = Hasil.get_by_id(request.view_args["id"])
    return jsonify(hasil)

@hasil_routes.route("/add", methods=['POST'])
def add():
    pekerjaan_id = request.json.get('pekerjaan_id')
    pekerja_id = request.json.get('pekerja_id')
    hasil = Hasil.add(pekerjaan_id,tipe_pekerja_id)
    return jsonify(hasil)

@hasil_routes.route("/delete", methods=['DELETE'])
def delete_by_id():
    id = request.json.get('id')
    hasil = Hasil.delete_by_id(id)
    return jsonify(hasil)


