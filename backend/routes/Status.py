from flask import Blueprint,request,jsonify,Response
from ..controller import Status
import json


Status_routes = Blueprint ('Status', __name__)

@Status_routes.route("/all", methods=['GET'])
def get_all():
    status = Status.get_all()
    return jsonify(status)

@Status_routes.route("/id/<id>", methods= ['GET'])
def get_by_id(id:int):
    status = Status.get_by_id(request.view_args["id"])
    return jsonify(status)

@Status_routes.route("/add", methods=['POST'])
def add():
    pekerjaan_id = request.json.get('pekerjaan_id')
    timestamp = request.json.get('timestamp')
    type = request.json.get('type')
    status = Status.add(pekerjaan_id,timestamp,type)
    return jsonify(status)