from flask import Blueprint, request, jsonify, Response
from ..controller import Pekerja
import json

pekerja_routes = Blueprint('Pekerja', __name__)

@pekerja_routes.route("/all", methods=['GET'])
def get_all():
    pekerja = Pekerja.get_all()
    return jsonify(pekerja)