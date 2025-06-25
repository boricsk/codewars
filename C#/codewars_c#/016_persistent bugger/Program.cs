/*
Írjon egy függvényt, a perzisztenciát, amely egy pozitív num paramétert vesz fel, 
és visszaadja a szorzós perzisztenciáját, ami annyiszor kell, hogy meg kell 
szoroznia a számjegyeket num-ban, amíg egy számjegyet nem kap.

Például (Input --> Output): 
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
*/
namespace _016_persistent_bugger
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //3*9 = 27 2*7 = 14 1*4 = 4
            Console.WriteLine(Persistence(39));
            Console.WriteLine(Persistence(4));
            Console.WriteLine(Persistence(25));
            Console.WriteLine(Persistence(999));

        }
        public static int Persistence(long n)
        {
            string num = "";
            int count = 0;
            int multiply = 1;
            if (n < 10) { return 0; }
            else
            {
                num = n.ToString();
            }

            while (num.Length != 1)
            {
                for (int i = 0; i < num.Length; i++)
                {
                    //A karakter átalakítása számmá
                    multiply *= (int)(num[i] - '0');
                }
                num = multiply.ToString();
                multiply = 1;
                count++;
            }

            return count;
            num.Reverse
        }
    }
}
