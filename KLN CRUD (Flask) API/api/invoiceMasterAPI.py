from flask import Flask, jsonify, Blueprint

from model.invoiceMaster import InvoiceMaster

from schema.invoiceMasterSchema import InvoiceMasterSchema


apiInvoiceMasters = Blueprint("apiInvoiceMasters", __name__, url_prefix="/api/invoicemasters")

invoiceMaster_schema = InvoiceMasterSchema()
invoiceMasters_schema = InvoiceMasterSchema(many=True)

@apiInvoiceMasters.route("/", methods=["GET"])
def getAllInvoiceMasters():
    try:
        invoiceMasters = InvoiceMaster.getAllInvoiceMasters()

        if invoiceMasters:
            result = invoiceMasters_schema.dump(invoiceMasters)
            return result
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiInvoiceMasters.route("/<int:id>", methods=["GET"])
def getInvoiceMasterById(id):
    try:
        invoiceMaster = InvoiceMaster.getInvoiceMasterById(id)

        if invoiceMaster == None:
            return jsonify({"message":"Object has not been found"})
        else:
            result = invoiceMaster_schema.dump(invoiceMaster)
            return jsonify({"invoiceMaster":result})
    except Exception as e:
        return jsonify({"success":False,"message":e})
