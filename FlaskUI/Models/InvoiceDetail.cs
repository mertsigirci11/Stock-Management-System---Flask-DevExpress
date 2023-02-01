using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models
{
    public class InvoiceDetail
    {
        public int amount { get; set; }
        public int id { get; set; }
        public int invoice_master_id { get; set; }
        public int pieces { get; set; }
        public int price { get; set; }
        public string productName { get; set; }
    }
}
