namespace _007_prime_streaming
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }

        public static IEnumerable<int> Stream()
        {
            int n = 15490000;
            bool[] prime_list = new bool[n + 1];
            for (int i = 0; i < prime_list.Length; i++)
            {
                prime_list[i] = true;
            }
            prime_list[0] = false;
            prime_list[1] = false;
            //elballagunk az n gyökéig + 1
            for (var i = 2; i * i <= n; i++)
            {
                //végigballagunk a listán úgy, hogy be tudjuk állítani i többszöröseire a false-t
                for (var j = 2 * i; j <= n; j += i)
                {
                    prime_list[j] = false;
                }
            }
            List<int> primes = new List<int>();
            for (var k = 0; k < prime_list.Length; k++)
            {
                if (prime_list[k])
                {
                    //Console.Write($"{k} ");
                    primes.Add(k);

                }
            }            
            return primes;
        }

        public static IEnumerable<int> Stream2()
        {
            int limit = 15490000;
            bool[] primes = new bool[limit];

            // Inicializáljuk az összes elemet True-ra
            for (int i = 0; i < limit; i++)
            {
                primes[i] = true;
            }

            // 0 és 1 nem prímek
            primes[0] = false;
            primes[1] = false;

            // Szita algoritmus
            for (int baseNum = 2; baseNum * baseNum <= limit; baseNum++)
            {
                if (primes[baseNum])
                {
                    for (int multiple = baseNum * 2; multiple < limit; multiple += baseNum)
                    {
                        primes[multiple] = false;
                    }
                }
            }

            // Eredmény generálása
            for (int i = 2; i < limit; i++)
            {
                if (primes[i])
                {
                    yield return i;
                }
            }
        }

    }
}
