from application import app
from application.resources.wash_services_resource import wash_service_bp
from flask_cors import CORS
from flask import send_from_directory

CORS(app)

# Serve frontend
@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

app.register_blueprint(wash_service_bp)
if __name__ == '__main__':
    app.run(debug=True)