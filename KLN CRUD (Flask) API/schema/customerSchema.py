from flask_marshmallow import Marshmallow

ma = Marshmallow()
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("id","name", "password",
                  "surname", "tax_administration",
                  "username")