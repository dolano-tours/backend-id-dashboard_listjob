from flask import Blueprint, request, jsonify, Response
from ..controller import Hasil
import json

hasil_routes = Blueprint('Hasil', __name__)

@hasil_routes.route("/all", methods=['GET'])
def get_all():
    hasil = Hasil.get_all()
    return jsonify(hasil)