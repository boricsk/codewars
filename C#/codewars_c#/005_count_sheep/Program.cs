/*
ha nem tudsz aludni, számold csak a birkákat!!
Feladat:

Adott egy nem negatív egész szám, például 3, adjon vissza egy karakterláncot 
mormolással: "1 bárány... 2 bárány... 3 bárány...". 
A bemenet mindig érvényes lesz, azaz nincsenek negatív egész számok. 
*/
namespace _005_count_sheep
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(CountSheep(1));
        }

        public static string CountSheep(int n)
        {
            string ret = "";
            if (n == 0) { return ""; }
            else
            {

                for (int i = 0; i < n; i++)
                {
                    ret += Convert.ToString(i+1) + " sheep...";
                }
            }
            return ret;
        }

    }

}
