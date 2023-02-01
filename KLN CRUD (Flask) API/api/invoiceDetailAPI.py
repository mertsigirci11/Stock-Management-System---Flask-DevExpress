from flask import Flask, jsonify, Blueprint

from model.invoiceDetail import InvoiceDetail

from schema.invoiceDetailSchema import InvoiceDetailSchema

apiInvoiceDetails = Blueprint("apiInvoiceDetails", __name__, url_prefix="/api/invoicedetails")

invoiceDetail_schema = InvoiceDetailSchema()
invoiceDetails_schema = InvoiceDetailSchema(many=True)

@apiInvoiceDetails.route("/", methods=["GET"])
def getAllInvoiceDetails():
    try:
        invoiceDetails = InvoiceDetail.getAllInvoiceDetails()

        if invoiceDetails:
            result = invoiceDetails_schema.dump(invoiceDetails)
            return jsonify({"count":len(result),"invoiceDetails":result})
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiInvoiceDetails.route("/<int:id>", methods=["GET"])
def getInvoiceDetailById(id):
    try:
        invoiceDetails = InvoiceDetail.getInvoiceDetailById(id) #invoiceMasterID

        if invoiceDetails == []:
            return jsonify({"message":"Object has not been found"})
        else:
            result = invoiceDetails_schema.dump(invoiceDetails)
            return result

    except Exception as e:
        return jsonify({"success":False,"message":e})

