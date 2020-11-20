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