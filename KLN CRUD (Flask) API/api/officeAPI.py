from flask import Flask, jsonify, Blueprint, request

from model.office import Office

from schema.officeSchema import OfficeSchema

apiOffices = Blueprint("apiOffices", __name__, url_prefix="/api/offices")

office_schema = OfficeSchema()
offices_schema = OfficeSchema(many=True)

@apiOffices.route("/", methods=["GET"])
def getOffices():
    try:
        offices = Office.getAllOffices()

        if offices:
            result = offices_schema.dump(offices)
            return result
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiOffices.route("/", methods=["POST"])
def createOffice():
    try:
        if (request.data):
            data = request.get_json()
            
            address = data["address"]
            name = data["name"]
            company_id = data["company_id"]

            Office.createOffice(address,name,company_id)

            office = Office("0",address,name,company_id)
            result = office_schema.dump(office)

            return {
                "message":"Operation is success", 
                "office":result
            }, 201

            #Marshmallow kullanmadan once asagidaki gibiydi

            #return jsonify(
             #   {
              #      "message":"Object has been created",
               #     "new office":
                #    {
                 #       "address":address,
                  #      "name":name, 
                   #     "company_id":company_id
                    #}
                #})
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiOffices.route("/<int:id>", methods=["PUT"])
def putOffice(id):
    try:
        office = Office.getOfficeById(id)

        if office == None:
            return jsonify({"message":"Object has not been found"})
        else:
            data = request.get_json()
            
            idGet = id
            address = data["address"]
            name = data["name"]
            company_id = data["company_id"]

            Office.updateOffice(id,address,name,company_id)
            result = office_schema.dump(office)
            officeObjInf = {'id':idGet}
            officeObjInf.update(result)

            return {
                "message":"Object has been updated", 
                "office":officeObjInf
            }, 200

            #return jsonify(
            #    {
            #        "message":"Object has been updated",
            #        "office":
            #        {
            #            "address":address,
            #            "name":name, 
            #            "company_id":company_id
            #        }
            #    })

    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiOffices.route("<int:id>", methods=["DELETE"])
def deleteOffice(id):
    try:
        office = Office.getOfficeById(id)
        if office == None:
            return jsonify({"message":"Object has not been found"})
        else:
            Office.deleteOffice(id)
            return jsonify({"message":"Object has been deleted"})
    except Exception as e:
        return jsonify({"success":False,"message":e})

