/*
A szupermarketben sorba kell állni az önpénztári pénztáraknál. Az Ön feladata, 
hogy írjon egy függvényt, amely kiszámítja az összes ügyfél kijelentkezési idejét!

bemenet
ügyfelek: pozitív egész számok tömbje, amely a sort reprezentálja. Minden egész 
szám egy ügyfelet jelöl, értéke pedig a kijelentkezéshez szükséges idő.
n: pozitív egész szám, a pénztárak száma.

kimenet
A függvénynek egy egész számot kell visszaadnia, vagyis a szükséges teljes időt.

Példák
queueTime([5;3;4];1)
// 12-et kell visszaadnia
// mert amikor 1 meddig van, a teljes idő csak az idők összege

queueTime([10;2;3;3];2)
// 10-et kell visszaadnia, mert itt n=2, és a sorban lévő 2., 3. és 4. ember előbb végez, mint az 1. személy.

queueTime([2;3;10];2)
// 12-et kell visszaadnia

Pontopontosítások
Csak EGY sorban áll sok kassza kiszolgálására, és A sor sorrendje SOHA nem változik, és
A sorban álló első személy (azaz a tömb/lista első eleme) a kasszához lép, amint felszabadul.
N.B. Fel kell tételeznie, hogy az összes tesztbevitel érvényes lesz, a fent leírtak szerint.

P.S. A helyzet ebben a katában hasonlítható a számítógép-tudományokkal kapcsolatos 
szálkészlet ötletéhez, több folyamat egyidejű futtatásához: https://en.wikipedia.org/wiki/Thread_pool
 */

namespace _018_the_supermarket_queue
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] test1 = { 5, 3, 4 };
            int[] test2 = { 10, 2, 3, 3 };
            int[] test3 = { 2, 3, 10 };

            Console.WriteLine(QueueTime(test1, 1));
            Console.WriteLine(QueueTime(test2, 2));
            Console.WriteLine(QueueTime(test3, 100));

        }
        public static long QueueTime(int[] customers, int n)
        {
            long ret = 0;
            int[] self_checkouts = new int[n];

            if (n == 1) { ret = customers.Sum(); }
            else if (customers.Length == 0 || customers == null) { ret = 0; }
            else if (n >= customers.Length) { ret = customers.Max(); }
            else
            {
                foreach (int customer in customers)
                {
                    self_checkouts[0] += customer;
                    Array.Sort(self_checkouts);
                }
                ret = self_checkouts.Max();
            }

            return ret;
        }

    }
}
