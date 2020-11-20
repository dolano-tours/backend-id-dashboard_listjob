from flask import Flask
from backend.config.database import init_db,db_session
from backend.routes.TipePekerja import tipe_pekerja_routes
from backend.routes.Pekerjaan import pekerjaan_routes
from backend.routes.Pekerja import pekerja_routes
from backend.routes.Hasil import hasil_routes
from backend.routes.Document import document_routes

app = Flask("dashboard")