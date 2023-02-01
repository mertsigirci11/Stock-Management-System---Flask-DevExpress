from flask import Flask, jsonify, Blueprint, request

from model.customer import Customer

from schema.customerSchema import CustomerSchema

apiCustomers = Blueprint("apiCustomers", __name__, url_prefix="/api/customers")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@apiCustomers.route("/", methods=["GET"])
def getCustomers():
    try:
        customers = Customer.getAllCustomers()

        if customers:
            result = customers_schema.dump(customers)                
            return result
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiCustomers.route("/", methods=["POST"])
def createCustomer():
    try:
        if (request.data):
            data = request.get_json()
            
            name = data["name"]
            password = data["password"]
            surname = data["surname"]
            tax_administration = data["tax_administration"]
            username = data["username"]

            Customer.createCustomer(name,password,surname,tax_administration,username)

            customer = Customer("0",name,password,surname,tax_administration,username)
            result = customer_schema.dump(customer)

            return {
                "message":"Operation is success", 
                "customer":result
            }, 201

            #Marshmallow kullanmadan once asagidaki gibiydi

            #return jsonify(
                #{
               #     "message":"Object has been created",
               #     "new customer":
               #     {
               #         "name":name, "password":password, "surname":surname,
               #         "tax_administration":tax_administration,"username":username
               #     }
               # })
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiCustomers.route("/<int:id>", methods=["PUT"])
def putCustomer(id):
    try:
        customer = Customer.getCustomerById(id)

        if customer == None:
            return jsonify({"message":"Object has not been found"})
        else:
            data = request.get_json()
            
            idGet = id
            name = data["name"]
            password = data["password"]
            surname = data["surname"]
            tax_administration = data["tax_administration"]
            username = data["username"]

            Customer.updateCustomer(id,name,password,surname,tax_administration,username)
            customer1 = Customer(idGet,name,password,surname,tax_administration,username)
            result = customer_schema.dump(customer1)
            customerObjInf = {'id':idGet}
            customerObjInf.update(result)

            return {
                "message":"Object has been updated", 
                "customer":customerObjInf
            }, 200

            #return jsonify(
            #    {
            #        "message":"Object has been updated",
            #        "customer":
            #        {
            #            "name":name, "password":password, "surname":surname,
            #            "tax_administration":tax_administration,"username":username
            #        }
            #    })

    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiCustomers.route("<int:id>", methods=["DELETE"])
def deleteCustomer(id):
    try:
        customer = Customer.getCustomerById(id)
        if customer == None:
            return jsonify({"message":"Object has not been found"})
        else:
            Customer.deleteCustomer(id)
            return jsonify({"message":"Object has been deleted"})
    except Exception as e:
        return jsonify({"success":False,"message":e})

