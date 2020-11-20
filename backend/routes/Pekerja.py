from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerja
import json

pekerja_routes = Blueprint('Pekerja', __name__)

@pekerja_routes.route("/all", methods=['GET'])
def get_all():
    pekerja = Pekerja.get_all()
    return jsonify(pekerja)

@pekerja_routes.route("/id/<id>", methods=['GET'])
def get_by_id(id:int):
    pekerja = Pekerja.get_by_id(request.view_args["id"])
    return jsonify(pekerja)
