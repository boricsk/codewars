/*
Timmy és Sarah azt hiszik, hogy szerelmesek, de lakóhelyük körül csak akkor tudják meg, 
ha leszednek egy-egy virágot. Ha az egyik virágnak páros, a másiknak páratlan számú 
szirmja van, az azt jelenti, hogy szerelmesek.

Írjon egy függvényt, amely felveszi az egyes virágok szirmainak számát, és igazat 
ad vissza, ha szerelmes, és hamis, ha nem. 
*/
namespace _006_tim_and_sarah
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    Console.WriteLine($"Flowers {i} : {j} {lovefunc2(i, j)}");
                }
            }
        }
        public static bool lovefunc(int flower1, int flower2)
        {
            return !((flower1 % 2 == 0) && (flower2 % 2 == 0) || (flower1 % 2 != 0) && (flower2 % 2 != 0));
        }

        public static bool lovefunc2(int flower1, int flower2)
        {
            return (flower1 + flower2) % 2 != 0;
        }
    }
}
