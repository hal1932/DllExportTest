using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsApp
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var test = new CsTestClass())
            {
                Console.WriteLine(test.Func1(1));
                Console.WriteLine(test.Func2(i => i + 2, 1));
            }
            Console.ReadKey();
        }
    }
}
