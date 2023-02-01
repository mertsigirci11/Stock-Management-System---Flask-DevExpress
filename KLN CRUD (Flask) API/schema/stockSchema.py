from flask_marshmallow import Marshmallow

ma = Marshmallow()
class StockSchema(ma.Schema):
    class Meta:
        fields = ("id","name","piece","price","warehouse_id")