from flask import Blueprint,request,jsonify,Response
from ..controller import Status
from flask_cors import cross_origin
import json



Status_routes = Blueprint ('Status', __name__)

@Status_routes.route("/all", methods=['GET'])
@cross_origin()
def get_all():
    status = Status.get_all()
    return jsonify(status)

@Status_routes.route("/id/<id>", methods= ['GET'])
@cross_origin()
def get_by_id(id:int):
    status = Status.get_by_id(request.view_args["id"])
    return jsonify(status)

@Status_routes.route("/add", methods=['POST'])
@cross_origin()
def add():
    pekerjaan_id = request.json.get('pekerjaan_id')
    timestamp = request.json.get('timestamp')
    typez = request.json.get('type')
    status = Status.add(pekerjaan_id,timestamp,typez)
    return jsonify(status)

@Status_routes.route("/delete", methods=['POST'])
@cross_origin()
def delete():
    id = request.json.get('id')
    status = Status.delete_by_id(id)
    return jsonify(status)


@Status_routes.route("/update", methods=['PUT'])
@cross_origin()
def update_by_id():
    id = request.json.get('id')
    typez = request.json.get('type')
    
    status = Status.update_by_id(id,typez)
    return jsonify(status)