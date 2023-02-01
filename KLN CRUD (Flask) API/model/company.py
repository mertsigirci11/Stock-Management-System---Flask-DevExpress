from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship


@dataclass
class Company(db.Model):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    email = db.Column(db.String(60))
    name = db.Column(db.String(30))
    password = db.Column(db.String(30))
    phone = db.Column(db.String(20))
    tax_number = db.Column(db.String(15))
    username = db.Column(db.String(20))
    warehouses = db.relationship("Warehouse",backref="company")
    offices = db.relationship("Office",backref="company")

    def __init__(self,id,address,email,name,password,phone,tax_number,username):
        self.id = id
        self.address = address
        self.email = email
        self.name = name
        self.password = password
        self.phone = phone
        self.tax_number = tax_number
        self.username = username

    @classmethod
    def createCompany(cls,address,email,name,password,phone,tax_number,username):
        company = cls(None,address,email,name,password,phone,tax_number,username)
        db.session.add(company)
        db.session.commit()

    @classmethod
    def getAllCompanies(cls):
        return cls.query.all()

    @classmethod
    def getCompanyById(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def updateCompany(cls,id,address,email,name,password,phone,tax_number,username):
        company = cls.query.filter_by(id=id).first()
        company.address = address
        company.email = email
        company.name = name
        company.password = password
        company.phone = phone
        company.tax_number = tax_number
        company.username = username
        db.session.commit()

    @classmethod
    def deleteCompany(cls,id):
        company = cls.query.filter_by(id=id).first()
        db.session.delete(company)
        db.session.commit()
