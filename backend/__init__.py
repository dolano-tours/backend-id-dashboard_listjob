from flask import Flask
from backend.config.database import init_db,db_session

from backend.routes.Pekerjaan import pekerjaan_routes
from backend.routes.Pekerja import pekerja_routes


app = Flask("dashboard")
