from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship

@dataclass
class Customer(db.Model):
    __tablename__ = "customer"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(20))
    surname = db.Column(db.String(30))
    tax_administration = db.Column(db.String(15))
    username = db.Column(db.String(20))
    invoice_masters = db.relationship("InvoiceMaster",backref="customer")

    def __init__(self,id,name,password,surname,tax_administration,username):
        self.id = id
        self.name = name
        self.password = password
        self.surname = surname
        self.tax_administration = tax_administration
        self.username = username

    @classmethod
    def createCustomer(cls,name,password,surname,tax_administration,username):
        customer = cls(None,name,password,surname,tax_administration,username)
        db.session.add(customer)
        db.session.commit()

    @classmethod
    def getAllCustomers(cls):
        return cls.query.all()

    @classmethod
    def getCustomerById(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def updateCustomer(cls,id,name,password,surname,tax_administration,username):
        customer = cls.query.filter_by(id=id).first()
        customer.name = name
        customer.password = password
        customer.surname = surname
        customer.tax_administration = tax_administration
        customer.username = username
        db.session.commit()

    @classmethod
    def deleteCustomer(cls,id):
        customer = cls.query.filter_by(id=id).first()
        db.session.delete(customer)
        db.session.commit()