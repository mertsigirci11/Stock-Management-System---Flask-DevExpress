from flask_marshmallow import Marshmallow

ma = Marshmallow()
class WarehouseSchema(ma.Schema):
    class Meta:
        fields = ("id","name","company_id")