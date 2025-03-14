from application import app
from application.resources.wash_services_resource import wash_service_bp
from flask_cors import CORS

CORS(app)

app.register_blueprint(wash_service_bp)
if __name__ == '__main__':
    app.run(debug=True)