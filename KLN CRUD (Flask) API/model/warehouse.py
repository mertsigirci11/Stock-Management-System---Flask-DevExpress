from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship

@dataclass
class Warehouse(db.Model):
    __tablename__ = "warehouse"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    stocks = db.relationship("Stock",backref="warehouse")

    def __init__(self,id,name,company_id):
        self.id = id
        self.name = name
        self.company_id = company_id

    @classmethod
    def createWarehouse(cls,name,company_id):
        warehouse = cls(None,name,company_id)
        db.session.add(warehouse)
        db.session.commit()

    @classmethod
    def getAllWarehouses(cls):
        return cls.query.all()

    @classmethod
    def getWarehouseById(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def updateWarehouse(cls,id,name,company_id):
        warehouse = cls.query.filter_by(id=id).first()
        warehouse.name = name
        warehouse.company_id = company_id
        db.session.commit()

    @classmethod
    def deleteWarehouse(cls,id):
        warehouse = cls.query.filter_by(id=id).first()
        db.session.delete(warehouse)
        db.session.commit()