from flask import Flask, jsonify, Blueprint, request

from model.stock import Stock

from schema.stockSchema import StockSchema

apiStocks = Blueprint("apiStocks", __name__, url_prefix="/api/stocks")

stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)

@apiStocks.route("/", methods=["GET"])
def getStocks():
    try:
        stocks = Stock.getAllStocks()

        if stocks:
            result = stocks_schema.dump(stocks)
            return result
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiStocks.route("/", methods=["POST"])
def createStock():
    try:
        if (request.data):
            data = request.get_json()
            
            name = data["name"]
            piece = data["piece"]
            price = data["price"]
            warehouse_id = data["warehouse_id"]

            Stock.createStock(name,piece,price,warehouse_id)
            
            stock = Stock("0",name,piece,price,warehouse_id)
            result = stock_schema.dump(stock)

            return {
                "message":"Operation is success", 
                "stock":result
            }, 201

            #Marshmallow kullanmadan once asagidaki gibiydi

            #return jsonify(
             #   {
              #      "message":"Object has been created",
               #     "new stock":
                #    {
                 #       "name":name, 
                  #      "piece":piece, 
                   #     "price":price,
                    #    "warehouse_id":warehouse_id
                    #}
                #})
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiStocks.route("/<int:id>", methods=["PUT"])
def putStock(id):
    try:
        stock = Stock.getStockById(id)

        if stock == None:
            return jsonify({"message":"Object has not been found"})
        else:
            data = request.get_json()
            
            idGet = id
            name = data["name"]
            piece = data["piece"]
            price = data["price"]
            warehouse_id = data["warehouse_id"]

            Stock.updateStock(id,name,piece,price,warehouse_id)
            stock1 = Stock(id,name,piece,price,warehouse_id)
            result = stock_schema.dump(stock1)
            stockObjInf = {'id':idGet}
            stockObjInf.update(result)

            return {
                "message":"Object has been updated", 
                "stock":stockObjInf
            }, 200

            #return jsonify(
            #    {
            #        "message":"Object has been updated",
            #        "stock":
            #        {
            #            "name":name, 
            #            "piece":piece, 
            #            "price":price,
            #            "warehouse_id":warehouse_id
            #        }
            #    })

    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiStocks.route("<int:id>", methods=["DELETE"])
def deleteStock(id):
    try:
        stock = Stock.getStockById(id)
        if stock == None:
            return jsonify({"message":"Object has not been found"})
        else:
            Stock.deleteStock(id)
            return jsonify({"message":"Object has been deleted"})
    except Exception as e:
        return jsonify({"success":False,"message":e})
