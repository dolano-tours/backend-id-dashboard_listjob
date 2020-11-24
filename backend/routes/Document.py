from flask import Blueprint, request, jsonify, Response
from ..controller import Document
import json

document_routes = Blueprint('Document', __name__)

@document_routes.route("/all", methods=['GET'])
def get_all():
    document = Document.get_all()
    return jsonify(document)

@document_routes.route("/id/<id>", methods=['GET'])
def get_by_id(id:int):
    
    document = Document.get_by_id(request.view_args["id"])
    return jsonify(document)

@document_routes.route("/delete", methods=['DELETE'])
def delete_by_id():
    id = request.json.get('id')
    document = Document.delete_by_id(id)
    return jsonify(document)

@document_routes.route("/add", methods=['POST'])
def add():
    pekerjaan_id = request.json.get('pekerjaan_id')
    pekerja_id = request.json.get('pekerja_id')
    document = Document.add(pekerjaan_id,tipe_pekerja_id)
    return jsonify(document)

@document_routes.route("/update/id", methods=['POST'])
def update_by_id():
    target_id = request.json.get('get_id')
    path_file = request.json.get('get_nama')

    document = Document.update_by_id(target_id, path_file)
    return jsonify(document)


