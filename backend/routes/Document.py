from flask import Blueprint, request, jsonify, Response
from ..controller import Document
import json

document_routes = Blueprint('Document', __name__)

@document_routes.route("/all", methods=['GET'])
def get_all():
    document = Document.get_all()
    return jsonify(document)

@document_routes.route("/id/<id>", methods=['GET'])
def get_by_id(id:int):
    
    document = Document.get_by_id(request.view_args["id"])
    return jsonify(document)