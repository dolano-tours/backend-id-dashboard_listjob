from flask import Blueprint, request, jsonify, Response
from .. import TipePekerjaSchema
from ..controller import TipePekerja
from ..models.model import TipePekerja as TipePekerjaModel
import json


tipe_pekerja_routes = Blueprint('TipePekerja', __name__)

@tipe_pekerja_routes.route("/all", methods=['GET'])
def get_all():
    tipe_pekerja = TipePekerja.get_all()
    return TipePekerjaSchema.dump(tipe_pekerja)