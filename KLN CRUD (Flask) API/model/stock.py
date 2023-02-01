from dataclasses import dataclass
from crud import db
from sqlalchemy.orm import relationship

class Stock(db.Model):
    __tablename__ = "stock"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    piece = db.Column(db.Integer)
    price = db.Column(db.Integer)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"))

    def __init__(self,id,name,piece,price,warehouse_id):
        self.id = id
        self.name = name
        self.piece = piece
        self.price = price
        self.warehouse_id = warehouse_id

    @classmethod
    def createStock(cls,name,piece,price,warehouse_id):
        stock = cls(None,name,piece,price,warehouse_id)
        db.session.add(stock)
        db.session.commit()

    @classmethod
    def getAllStocks(cls):
        return cls.query.all()

    @classmethod
    def getStockById(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def updateStock(cls,id,name,piece,price,warehouse_id):
        stock = cls.query.filter_by(id=id).first()
        stock.name = name
        stock.piece = piece
        stock.price = price
        stock.warehouse_id = warehouse_id
        db.session.commit()

    @classmethod
    def deleteStock(cls,id):
        stock = cls.query.filter_by(id=id).first()
        db.session.delete(stock)
        db.session.commit()     