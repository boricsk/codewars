/*
Bob buszsofőrként dolgozik. A város lakossága körében azonban rendkívül népszerűvé vált. 
Mivel sok utas szeretne felszállni a buszára, néha szembe kell néznie azzal a problémával, 
hogy nincs elég hely a buszon! Azt akarja, hogy írjon egy egyszerű programot, amely 
megmondja neki, hogy képes lesz-e elvinni az összes utast.

Feladat áttekintése:

Olyan függvényt kell írni, amely három paramétert fogad el:
 A felső határ a busz befogadására alkalmas személyek száma, a sofőr nélkül.
 a buszon tartózkodók száma, a sofőr nélkül.
 a várakozás a buszra várakozók száma, a sofőr nélkül.

Ha van elég hely, adjon vissza 0-t, és ha nincs, adja vissza azt az utasszámot, amelyet nem tud elvinni.

Használati példák:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting

*/
namespace _003_will_there_be_enough_space
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
        public static int Enough(int cap, int on, int wait)
        {
            return (cap < (on + wait)) ? (on + wait) - cap : 0; 
        }
    }
}
