/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
 */
namespace _020_find_unique_number
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(GetUnique([1, 1, 1, 2, 1, 1]));
        }
        public static int GetUnique(IEnumerable<int> numbers)
        {
            // Csoportképzés az értékek alapján
            var occurences = numbers.GroupBy(x => x)
                .Select(g => new { number = g.Key, Count = g.Count()})  //Lekéri az egyes csoportok (számok) érékét és azok előfordulásait
                .Where(x => x.Count == 1)                               //, ahol az előfordulás 1.
                .FirstOrDefault();                                      //az első előfordulás lekérése, ha több van hiba lesz.

            return (occurences !=null) ? occurences.number : 0;
            //foreach (var item in occurences)
            //{
            //    return item.number;
            //}

            //return 0;
        }
    }
}
