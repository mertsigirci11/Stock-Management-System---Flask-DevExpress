using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models
{
    public class InvoiceMaster
    {
            public string customer_bank_account_number { get; set; }
            public int customer_id { get; set; }
            public string customer_name { get; set; }
            public string customer_tax_administration { get; set; }
            public DateTime date_time { get; set; }
            public int id { get; set; }
            public int office_id { get; set; }
            public int price { get; set; }
            public string string_price { get; set; }
            public int total_price { get; set; }
            public int vat { get; set; }
    }
}
