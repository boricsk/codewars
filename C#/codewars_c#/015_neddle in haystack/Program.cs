/*
Megtalálod a tűt a szénakazalban?

Írjon egy findNeedle() függvényt, amely egy szeméttel teli tömböt tartalmaz, de egy "tűt" tartalmaz
Miután a függvény megtalálta a tűt, egy üzenetet kell visszaadnia (karakterláncként), amely azt mondja:
"találta a tűt a pozícióban" plusz az index, hogy megtalálta a tűt, tehát:

Példa (Bemenet --> Kimenet)
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
 */
namespace _015_neddle_in_haystack
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var haystack_1 = new object[] { '3', "123124234", null, "needle", "world", "hay", 2, '3', true, false };
            var haystack_2 = new object[] { "283497238987234", "a dog", "a cat", "some random junk", "a piece of hay", "needle", "something somebody lost a while ago" };
            var haystack_3 = new object[] { 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3, 4, 2, 34, 234, 23, 4, 234, 324, 324, "needle", 1, 2, 3, 4, 5, 5, 6, 5, 4, 32, 3, 45, 54 };
            var haystack_4 = new Object[] { "junk", "more junk", new String("needle"), "gadget" };
            Console.WriteLine(FindNeedle(haystack_3));
            Console.WriteLine(FindNeedle(haystack_2));
            Console.WriteLine(FindNeedle(haystack_1));
            Console.WriteLine(FindNeedle(haystack_4));
        }
        public static string FindNeedle(object[] haystack)
        {
            int pos = 0;
            foreach (object item in haystack)
            {
                //Console.WriteLine(item);
                if (item is string && item.Equals("needle")) // (item == "needle") objektumként van létrehozva
                {
                    break;
                }
                pos++;
            }
            return $"found the needle at position {pos}";
        }
    }
}

