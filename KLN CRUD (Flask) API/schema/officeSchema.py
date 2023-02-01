from flask_marshmallow import Marshmallow

ma = Marshmallow()
class OfficeSchema(ma.Schema):
    class Meta:
        fields = ("id","address","name","company_id")