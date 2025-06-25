/*
Megkérdezed egy kislánytól: "Hány éves vagy?" Mindig azt mondja, hogy 
"x éves", ahol x egy véletlen szám 0 és 9 között.

Írjon programot, amely a lány életkorát (0-9) egész számként adja vissza!
Tegyük fel, hogy a teszt bemeneti karakterlánc mindig érvényes karakterlánc. 
Például a tesztbevitel lehet „1 éves” vagy „5 éves”. A karakterlánc első karaktere mindig egy szám.
*/
namespace _008_Parse_nice_int_from_char_problem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
        public static int GetAge(string inputString)
        {
            string ret = "";
            for (int i = 0; i < inputString.Length; i++)
            {
                if (char.IsDigit(inputString[i])) { ret += inputString[i]; }
            }
            return int.Parse(ret);
        }

    }
}
