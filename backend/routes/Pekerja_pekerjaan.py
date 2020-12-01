from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerja_pekerjaan
import json


pekerja_pekerjaan_routes = Blueprint('Pekerja_pekerjaan', __name__)

@pekerja_pekerjaan_routes.route("/all", methods=['GET'])
def get_all():
    pekerja_pekerjaan = Pekerja_pekerjaan.get_all()
    return jsonify(pekerja_pekerjaan)

@pekerja_pekerjaan_routes.route("/add", methods=['POST'])#add sesuai dengan ID dan id employee yang ada dalam database Pekerja 
def add():
    pekerja_id = request.json.get('pekerja_id')
    pekerjaan_id = request.json.get('pekerjaan_id')
    position = request.json.get('position')
    pekerja_pekerjaan = Pekerja_pekerjaan.add(pekerja_id,pekerjaan_id,position)
    return jsonify(pekerja_pekerjaan)

@pekerja_pekerjaan_routes.route("/delete", methods=['POST'])
def delete_by_id(): 
    pekerja_id = request.json.get('pekerja_id') 
    pekerjaan_id = request.json.get('pekerjaan_id')
    position = request.json.get('position')
    pekerja_pekerjaan = Pekerja_pekerjaan.delete_by_id(pekerjaan_id,pekerja_id,position)
    return jsonify(pekerja_pekerjaan)
    
@pekerja_pekerjaan_routes.route("/update", methods=['PUT'])
def update_by_position():
    position = request.json.get('position')
    pekerjaan_id = request.json.get('pekerjaan_id')
    pekerja_id = request.json.get('pekerja_id')
    pekerja_pekerjaan = Pekerja_pekerjaan.update_by_position(position,pekerjaan_id,pekerja_id)
    return jsonify(pekerja_pekerjaan)