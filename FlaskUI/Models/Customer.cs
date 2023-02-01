using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models
{
    public class Customer
    {
        public int id { get; set; }
        public string name { get; set; }
        public string password { get; set; }
        public string surname { get; set; }
        public string tax_administration { get; set; }
        public string username { get; set; }
    }
}
