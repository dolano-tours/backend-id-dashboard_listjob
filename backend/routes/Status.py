from flask import Blueprint,request,jsonify,Response
from ..controller import Status
import json


Status_routes = Blueprint ('Status', __name__)

@Status_routes.route("/all", methods=['GET'])
def get_all():
    status = Status.get_all()
    return jsonify(status)