from application import app
from application.resources.wash_services_resource import  wash_service_bp

from application.resources.customers_resource import customer_detail_bp
app.register_blueprint(wash_service_bp)

app.register_blueprint(customer_detail_bp)



if __name__ == '__main__':
    app.run(debug=True)