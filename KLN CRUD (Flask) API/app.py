from flask import Flask, jsonify,render_template,send_from_directory
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from pathlib import Path

from api.companyAPI import apiCompanies
from api.customerAPI import apiCustomers
from api.invoiceDetailAPI import apiInvoiceDetails
from api.invoiceMasterAPI import apiInvoiceMasters
from api.officeAPI import apiOffices
from api.stockAPI import apiStocks
from api.warehouseAPI import apiWarehouses

from crud import createApp



app = createApp()
CORS(app)


app.register_blueprint(apiCompanies)
app.register_blueprint(apiCustomers)
app.register_blueprint(apiInvoiceDetails)
app.register_blueprint(apiInvoiceMasters)
app.register_blueprint(apiOffices)
app.register_blueprint(apiStocks)
app.register_blueprint(apiWarehouses)

BASE_PATH = Path(__file__).resolve().parent
### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = "/static/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "KLN CRUD .v3"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/static/swagger.json")
def specs():
    return send_from_directory(BASE_PATH.joinpath('static'), 'swagger.json')

@app.route("/")
def index():
    return jsonify({"success":True, "message":"Main Page"})

if __name__ == "__main__":
    app.run(debug=True)