from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship

@dataclass
class InvoiceDetail(db.Model):
    __tablename__ = "invoice_detail"

    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer)
    pieces = db.Column(db.Integer)
    price = db.Column(db.Integer)
    productName = db.Column(db.String(30))
    invoice_master_id = db.Column(db.Integer, db.ForeignKey("invoice_master.id"))

    def __init__(self,id,amount,pieces,price,productName,invoice_master_id):
        self.id = id
        self.amount = amount
        self.pieces = pieces
        self.price = price
        self.productName = productName
        self.invoice_master_id = invoice_master_id

    @classmethod
    def getAllInvoiceDetails(cls):
        return cls.query.all()

    @classmethod
    def getInvoiceDetailById(cls,id):
        invoiceDetails = cls.query.all()
        listForId = []

        for invoiceDetail in invoiceDetails:
            if invoiceDetail.invoice_master_id == id:
                listForId.append(invoiceDetail)

        return listForId
        #return cls.query.filter_by(id=id).first()
