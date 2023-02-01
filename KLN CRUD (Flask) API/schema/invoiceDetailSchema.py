from flask_marshmallow import Marshmallow

ma = Marshmallow()
class InvoiceDetailSchema(ma.Schema):
    class Meta:
        fields = ("id", "amount", "pieces",
                  "price", "productName",
                  "invoice_master_id")