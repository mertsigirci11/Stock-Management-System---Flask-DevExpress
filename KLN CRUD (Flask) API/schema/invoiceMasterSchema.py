from flask_marshmallow import Marshmallow

ma = Marshmallow()
class InvoiceMasterSchema(ma.Schema):
    class Meta:
        fields = ("id", "customer_bank_account_number", "customer_name",
                  "customer_tax_administration", "date_time", "price",
                  "string_price", "total_price", "vat", "customer_id",
                  "office_id")