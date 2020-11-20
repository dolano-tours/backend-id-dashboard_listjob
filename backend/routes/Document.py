from flask import Blueprint, request, jsonify, Response
from ..controller import Document
import json

document_routes = Blueprint('Document', __name__)

@document_routes.route("/all", methods=['GET'])
def get_all():
    document = Document.get_all()
    return jsonify(document)