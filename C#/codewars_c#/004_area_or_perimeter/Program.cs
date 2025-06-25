/*
Megadjuk egy 4 oldalú sokszög hosszát és szélességét. A sokszög lehet téglalap vagy négyzet.
Ha négyzet, adja vissza a területét. Ha téglalap, adja vissza a kerületét.

Példa (Input1, Input2 --> Output):
6, 10 --> 32
3, 3 --> 9
*/
namespace _004_area_or_perimeter
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
        public class MathCheck
        {
            public static int AreaOrPerimeter(int l, int w)
            {
                return (l == w) ? (l * l) : (l + w) * 2;
            }
        }
    }
}
