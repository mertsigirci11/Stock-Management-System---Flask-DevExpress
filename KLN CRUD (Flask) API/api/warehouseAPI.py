from flask import Flask, jsonify, Blueprint, request

from model.warehouse import Warehouse

from schema.warehouseSchema import WarehouseSchema


apiWarehouses = Blueprint("apiWarehouses", __name__, url_prefix="/api/warehouses")

warehouse_schema = WarehouseSchema()
warehouses_schema = WarehouseSchema(many=True)

@apiWarehouses.route("/", methods=["GET"])
def getWarehouses():
    try:
        warehouses = Warehouse.getAllWarehouses()

        if warehouses:
            result = warehouses_schema.dump(warehouses)
            return result
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiWarehouses.route("/", methods=["POST"])
def createWarehouse():
    try:
        if (request.data):
            data = request.get_json()
            
            name = data["name"]
            company_id = data["company_id"]

            Warehouse.createWarehouse(name,company_id)

            warehouse = Warehouse("0",name,company_id)
            result = warehouse_schema.dump(warehouse)

            return {
                "message":"Operation is success", 
                "warehouse":result
            }, 201

            #Marshmallow kullanmadan once asagidaki gibiydi

            #return jsonify(
            #    {
            #        "message":"Object has been created",
            #        "new warehouse":
            #        {
            #            "name":name, 
            #            "company_id":company_id,
            #        }
            #    })
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiWarehouses.route("/<int:id>", methods=["PUT"])
def putWarehouse(id):
    try:
        warehouse = Warehouse.getWarehouseById(id)

        if warehouse == None:
            return jsonify({"message":"Object has not been found"})
        else:
            data = request.get_json()
            
            idGet = id
            name = data["name"]
            company_id = data["company_id"]

            Warehouse.updateWarehouse(id,name,company_id)
            warehouse1 = Warehouse(id,name,company_id)
            result = warehouse_schema.dump(warehouse1)
            warehouseObjInf = {'id':idGet}
            warehouseObjInf.update(result)

            return {
                "message":"Object has been updated", 
                "warehouse":warehouseObjInf
            }, 200

            #return jsonify(
            #    {
            #        "message":"Object has been updated",
            #        "warehouse":
            #        {
            #            "name":name, 
            #            "company_id":company_id,
            #        }
            #    })

    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiWarehouses.route("<int:id>", methods=["DELETE"])
def deleteWarehouse(id):
    try:
        warehouse = Warehouse.getWarehouseById(id)
        if warehouse == None:
            return jsonify({"message":"Object has not been found"})
        else:
            Warehouse.deleteWarehouse(id)
            return jsonify({"message":"Object has been deleted"})
    except Exception as e:
        return jsonify({"success":False,"message":e})
        