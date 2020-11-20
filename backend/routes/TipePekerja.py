from flask import Blueprint, request, jsonify, Response
from ..controller import TipePekerja
import json

tipe_pekerja_routes = Blueprint('TipePekerja', __name__)

@tipe_pekerja_routes.route("/all", methods=['GET'])
def get_all():
    tipe_pekerja = TipePekerja.get_all()
    return jsonify(tipe_pekerja)