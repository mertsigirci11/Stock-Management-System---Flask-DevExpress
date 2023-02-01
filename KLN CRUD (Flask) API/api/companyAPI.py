from flask import Flask, jsonify, Blueprint, request
from model.company import Company
from schema.companySchema import CompanySchema

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

apiCompanies = Blueprint("apiCompanies", __name__, url_prefix="/api/companies")

@apiCompanies.route("/",methods=["GET"])
def getAllCompanies():
    try:
        companies = Company.getAllCompanies()
        
        if companies:
            result = companies_schema.dump(companies)
            return result
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiCompanies.route("/",methods=["POST"])
def createCompany():
    try:
        if(request.data):
            data = request.get_json()
            
            address = data["address"]
            email = data["email"]
            name = data["name"]
            password = data["password"]
            phone = data["phone"]
            tax_number = data["tax_number"]
            username = data["username"]

            Company.createCompany(address,email,name,password,phone,tax_number,username)
            company = Company("0",address,email,name,password,phone,tax_number,username)
            result = company_schema.dump(company)
            
            return {
                "message":"Operation is success", 
                "company":result
            }, 201

            #Marshmallow kullanmadan once asagidaki gibiydi

            #return jsonify(
             #   {
              #      "message":"Operation is success", 
               #     "company":
                #    {
                 #       "address":address, "email":email,
                  #      "name":name, "password":password, "phone":phone,
                   #     "tax_number":tax_number, "username":username
                    #}
                #})
        else:
            return "No data", 400
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiCompanies.route("/<int:id>", methods=["PUT"])
def updateCompany(id):
    try:
        company = Company.getCompanyById(id)
        
        if company == None:
            return jsonify({"message":"Object has not been found"})
        else:
            data = request.get_json()
            
            idGet = id
            address = data["address"]
            email = data["email"]
            name = data["name"]
            password = data["password"]
            phone = data["phone"]
            tax_number = data["tax_number"]
            username = data["username"]

            Company.updateCompany(id,address,email,name,password,phone,tax_number,username)
            company1 = Company(idGet,address,email,name,password,phone,tax_number,username)
            result = company_schema.dump(company1)
            companyObjInf = {'id':idGet}
            companyObjInf.update(result)

            return {
                "message":"Object has been updated", 
                "company":companyObjInf
            }, 200

            #Marshmallow kullanmadan once asagidaki gibiydi

            #return jsonify(
            #    {
            #        "message":"Object has been updated",
            #        "company":
            #        {
            #            "id":company.id, "address":company.address, "email":company.email,
            #            "name":company.name, "password":company.password,
            #            "phone":company.phone,"tax_number":company.tax_number,
            #            "username":company.username
            #        }
            #    })
    except Exception as e:
        return jsonify({"success":False,"message":e})

@apiCompanies.route("/<int:id>",methods=["DELETE"])
def deleteCompany(id):
    try:
        company = Company.getCompanyById(id)
        if company == None:
            return jsonify({"message":"Object has not been found"})
        else:
            Company.deleteCompany(id)
            return jsonify({"message":"Object has been deleted"})
    except Exception as e:
        return jsonify({"success":False,"message":e})
    