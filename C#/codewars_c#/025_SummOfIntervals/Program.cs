/*
 Írj egy sumIntervals/sum_intervals nevű függvényt, amely intervallumok tömbjét fogadja el, és visszaadja az összes intervallumhossz összegét. 
Az átfedő intervallumokat csak egyszer kell számolni.

Intervallumok
Az intervallumokat egész számpárok ábrázolják tömb formájában. Az intervallum első értéke mindig kisebb lesz, mint a második érték. 
Intervallum példa: [1, 5] egy 1-től 5-ig terjedő intervallum. Ennek az intervallumnak a hossza 4.

Átfedő intervallumok
Átfedő intervallumokat tartalmazó lista:

[
[1, 4],
[7, 10],
[3, 5]
]
Ezen intervallumok hosszának összege 7. Mivel az [1, 4] és a [3, 5] átfedésben vannak, az intervallumot [1, 5]-ként kezelhetjük, 
amelynek hossza 4.

Példák
sumIntervals( [
   [1, 2],      1
   [6, 10],     4
   [11, 15]     4
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

1,4
3,5
7,10


sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

1,5
1,6
5,11
10,20
16,19



sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
 */

namespace _025_SummOfIntervals
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ValueTuple<int, int>[] intervals1 = new[] { (1, 2), (6, 10), (11, 15) };
            ValueTuple<int, int>[] intervals2 = new[] { (1, 4), (7, 10), (3, 5) };
            ValueTuple<int, int>[] intervals3 = new[] { (1, 5), (10, 20), (1, 6), (16, 19), (5, 11) };
            ValueTuple<int, int>[] intervals4 = new[] { (0, 20), (-100000000, 10), (30, 40) };

            int[][] example = new[]
{
            new[] { 1, 5 },
            new[] { 10, 20 },
            new[] { 1, 6 },
            new[] { 16, 19 },
            new[] { 5, 11 }
        };

            //Console.WriteLine(SumIntervals2(example)); // Kimenet: 19

            Console.WriteLine(SumIntervals3(intervals1));
            //Console.WriteLine(SumIntervals2(intervals2));
            //Console.WriteLine(SumIntervals2(intervals3));
            //Console.WriteLine(SumIntervals(intervals4));

        }
        public static int SumIntervals((int, int)[] intervals)
        {
            int ret = 0;
            int overlapSum = 0;
            List<ValueTuple<int, int>> tempIntervals = new List<ValueTuple<int, int>>();
            for (int i = 0; i < intervals.Length; i++)
            {
                for (int j = i + 1; j < intervals.Length; j++)
                {
                    var (a1, a2) = intervals[i]; //1,4
                    var (b1, b2) = intervals[j]; //3,5
                    if (a1 <= b2 && b1 <= a2)
                    {
                        //overlapSum += (b2 - a1);
                        tempIntervals.Add(new ValueTuple<int, int>(a1, b2));
                    }
                    else
                    {
                        tempIntervals.Add(new ValueTuple<int, int>(a1, a2));
                    }
                }
            }
            foreach (var interval in tempIntervals)
            {
                ret += (interval.Item2 - interval.Item1);
            }
            return ret;
        }

        public static int SumIntervals3((int, int)[] intervals)
        {
            if (intervals == null || intervals.Length == 0)
                return 0;

            // 1. Rendezzük az intervallumokat a kezdőpont szerint
            var sorted = intervals.OrderBy(i => i.Item1).ToList();

            // 2. Egyesített intervallumok listája
            List<(int, int)> merged = new List<(int, int)>();
            var current = sorted[0];

            foreach (var interval in sorted.Skip(1))
            {
                if (interval.Item1 <= current.Item2) // Átfedés
                {
                    current = (current.Item1, Math.Max(current.Item2, interval.Item2));
                }
                else
                {
                    merged.Add(current);
                    current = interval;
                }
            }
            merged.Add(current); // Ne felejtsük el az utolsót

            // 3. Összegzés
            return merged.Sum(i => i.Item2 - i.Item1);
        }



        public static int SumIntervals2(int[][] intervals)
        {
            if (intervals == null || intervals.Length == 0)
                return 0;

            // 1. Rendezzük az intervallumokat a kezdőpont szerint
            var sorted = intervals.OrderBy(i => i[0]).ToList();

            // 2. Egyesített intervallumok listája
            List<int[]> merged = new List<int[]>();
            int[] current = sorted[0];

            foreach (var interval in sorted.Skip(1))
            {
                if (interval[0] <= current[1]) // Átfedés
                {
                    current[1] = Math.Max(current[1], interval[1]);
                }
                else
                {
                    merged.Add(current);
                    current = interval;
                }
            }
            merged.Add(current); // Ne felejtsük el az utolsót

            // 3. Összegzés
            return merged.Sum(i => i[1] - i[0]);
        }
    }
}
