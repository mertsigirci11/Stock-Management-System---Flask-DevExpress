from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship

@dataclass
class Office(db.Model):
    __tablename__ = "office"

    id = db.Column(db.Integer,primary_key=True)
    address = db.Column(db.String(120))
    name = db.Column(db.String(30))
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    invoice_masters = db.relationship("InvoiceMaster",backref="office")

    def __init__(self,id,address,name,company_id):
        self.id = id
        self.address = address
        self.name = name
        self.company_id = company_id

    @classmethod
    def createOffice(cls,address,name,company_id):
        office = cls(None,address,name,company_id)
        db.session.add(office)
        db.session.commit()

    @classmethod
    def getAllOffices(cls):
        return cls.query.all()

    @classmethod
    def getOfficeById(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def updateOffice(cls,id,address,name,company_id):
        office = cls.query.filter_by(id=id).first()
        office.address = address
        office.name = name
        office.company_id = company_id
        db.session.commit()

    @classmethod
    def deleteOffice(cls,id):
        office = cls.query.filter_by(id=id).first()
        db.session.delete(office)
        db.session.commit()
