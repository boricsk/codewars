/*
A szám 
89
A 89 az első olyan egész szám, amely egynél több számjegyű, és amely részben megfelel a kata címében bemutatott tulajdonságnak. Mi értelme van azt mondani, hogy „heuréka”? Mert ez az összeg ugyanazt a számot adja: 
89 = 8^1 + 9^2  

A következő szám, amely rendelkezik ezzel a tulajdonsággal 
135
135:

Lásd ezt a tulajdonságot újra: 
135 = 1^1 + 3^2 + 5^3 = 1 + 9 + 125
 

Feladat
Szükségünk van egy függvényre, amely összegyűjti ezeket a számokat, és két egész számot kaphat. 
a,b. Amely meghatározza a tartományt [a,b] (inclusive), és a tartományban lévő rendezett számok listáját adja ki, amely megfelel a 
fent leírt tulajdonságnak.

Példa
1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

Ha nincs ilyen akkor üres lista legyen a visszatérés.
 */
using System.Collections;

namespace SummDigitPow
{
    internal class Program
    {
        static void Main(string[] args)
        {
            SumDigitPow2(1,1000);
        }
        public static long[] SumDigPow(long a, long b)
        {
            List<long> ret = new();
            for (long i = a; i <= b; i++)
            {
                string number = i.ToString();
                long digitpow = 0;
                for (int j = 1; j <= number.Length; j++)
                {                    
                    digitpow += (long)Math.Pow((int)number[j-1] - '0', j);
                    if (digitpow == i) { ret.Add(digitpow); }   
                }
            }

            return ret.ToArray();
        }
        public static void SumDigitPow2(long a, long b)
        {

            var ret = Enumerable.Range((int)a, (int)(b - a + 1))
           .Where(n => n == n.ToString()
               .Select((c, i) => Math.Pow(c - '0', i + 1))
               .Sum())
           .Select(n => (long)n)
           .ToArray();
        }

    }
}
