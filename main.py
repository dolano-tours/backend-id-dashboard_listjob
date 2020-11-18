from backend import app, init_db, tipe_pekerja_routes

init_db()
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.register_blueprint(tipe_pekerja_routes, url_prefix='/tipe_pekerja')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6969)

