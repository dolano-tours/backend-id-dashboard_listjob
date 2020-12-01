from flask import Blueprint, request, jsonify, Response
from ..controller import Aset
import json


Aset_routes = Blueprint('Aset', __name__)

@Aset_routes.route("/all", methods=['GET'])
def get_all():
    aset = Aset.get_all()
    return jsonify(aset)