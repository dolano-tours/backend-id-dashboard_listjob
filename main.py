from backend import app, init_db, tipe_pekerja_routes, pekerjaan_routes,pekerja_routes, hasil_routes, document_routes

from backend.config.database import *
init_db()
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.register_blueprint(tipe_pekerja_routes, url_prefix='/tipe_pekerja')
app.register_blueprint(pekerjaan_routes, url_prefix='/pekerjaan')
app.register_blueprint(pekerja_routes, url_prefix='/pekerja')
app.register_blueprint(hasil_routes, url_prefix='/hasil')
app.register_blueprint(document_routes, url_prefix='/document')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6969", debug=True)