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