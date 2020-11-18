from flask import Flask
from backend.config.database import init_db,db_session
from backend.routes.TipePekerja import tipe_pekerja_routes
from flask_marshmallow import Marshmallow


app = Flask("dashboard")