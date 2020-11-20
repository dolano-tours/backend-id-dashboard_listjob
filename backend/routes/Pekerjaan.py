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