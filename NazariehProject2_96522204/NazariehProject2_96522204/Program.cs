using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace NazariehProject2_96522204
{
    class Program
    {
        static void Main(string[] args)
        {
            var ReadData = ReadFile();
        }
        public static string[] ReadFile()
        {
            List<string> SaveList = new List<string>();

            using (StreamReader sr = new StreamReader(@"..\..\input.txt"))
            {

                string line;

                while ((line = sr.ReadLine()) != null)
                {

                    SaveList.Add(line);

                }
            }
            return SaveList.ToArray();

        }
    }
}
