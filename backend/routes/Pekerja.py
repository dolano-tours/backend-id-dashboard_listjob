from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerja
from flask_cors import cross_origin
import json

pekerja_routes = Blueprint('Pekerja', __name__)

@pekerja_routes.route("/all", methods=['GET'])
@cross_origin()
def get_all():
    pekerja = Pekerja.get_all()
    return jsonify(pekerja)

@pekerja_routes.route("/id/<id>", methods=['GET'])
@cross_origin()
def get_by_id(id:int):
    pekerja = Pekerja.get_by_id(request.view_args["id"])
    return jsonify(pekerja)


@pekerja_routes.route("/id_employee", methods=['GET'])
@cross_origin()
def get_by_id_employee(id_employee:int):
    pekerja = Pekerja.get_by_nama(request.view_args["id_employee"])
    return jsonify(pekerja)

@pekerja_routes.route("/add", methods=['POST'])
@cross_origin()
def add():
    id_employee = request.json.get('id_employee')
    pekerja = Pekerja.add(id_employee)
    return jsonify(pekerja)


@pekerja_routes.route("/delete", methods=['POST'])
@cross_origin()
def delete_by_id():
    id = request.json.get('id')
    pekerja = Pekerja.delete_by_id(id)
    return jsonify(pekerja)

@pekerja_routes.route("/update", methods=['PUT'])
@cross_origin()
def update_by_id():
    id = request.json.get('id')
    id_employee = request.json.get('id_employee')
    pekerja = Pekerja.update_by_id(id,id_employee)
    return jsonify(pekerja)
    