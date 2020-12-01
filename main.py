from backend import app, init_db,pekerjaan_routes,pekerja_routes,pekerja_pekerjaan_routes,Aset_routes,Status_routes
from backend.config.database import *
init_db()
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.register_blueprint(pekerjaan_routes, url_prefix='/pekerjaan')
app.register_blueprint(pekerja_routes, url_prefix='/pekerja')
app.register_blueprint(pekerja_pekerjaan_routes, url_prefix='/pekerja_pekerjaan')
app.register_blueprint(Aset_routes, url_prefix='/Aset')
app.register_blueprint(Status_routes, url_prefix='/Status')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6969", debug=True)