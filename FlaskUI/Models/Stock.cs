using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models
{
    public class Stock
    {
        public int id { get; set; }
        public string name { get; set; }
        public int piece { get; set; }
        public int price { get; set; }
        public int warehouse_id { get; set; }
    }
}
