from flask_marshmallow import Marshmallow

ma = Marshmallow()
class CompanySchema(ma.Schema):
    class Meta:
        fields = ("id","address", "email",
                  "name", "password",
                  "phone","tax_number","username")