from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship

@dataclass
class InvoiceMaster(db.Model):
    __tablename__ = "invoice_master"

    id = db.Column(db.Integer,primary_key=True)
    customer_bank_account_number = db.Column(db.String(15))
    customer_name = db.Column(db.String(30))
    customer_tax_administration = db.Column(db.String(15))
    date_time = db.Column(db.DateTime)
    price = db.Column(db.Integer)
    string_price = db.Column(db.String(30))
    total_price = db.Column(db.Integer)
    vat = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    office_id = db.Column(db.Integer, db.ForeignKey("office.id"))
    invoice_details = db.relationship("InvoiceDetail",backref="invoice_master")

    def __init__(self,id,customer_bank_account_number,customer_name,customer_tax_administration,
                date_time,price,string_price,total_price,vat,customer_id,office_id):
        self.id = id
        self.customer_bank_account_number = customer_bank_account_number
        self.customer_name = customer_name
        self.customer_tax_administration = customer_tax_administration
        self.date_time = date_time
        self.price = price
        self.string_price = string_price
        self.total_price = total_price
        self.vat = vat
        self.customer_id = customer_id
        self.office_id = office_id

    @classmethod
    def getAllInvoiceMasters(cls):
        return cls.query.all()

    @classmethod
    def getInvoiceMasterById(cls,id):
        return cls.query.filter_by(id=id).first()

    