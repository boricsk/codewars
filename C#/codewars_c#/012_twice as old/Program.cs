/*
A függvénynek két argumentuma van:

 apa jelenlegi életkora (év)
 fia jelenlegi életkora (év)

Számolja ki, hány évvel ezelőtt az apa volt kétszer annyi idős, 
mint a fia (vagy hány év múlva lesz kétszer annyi). A válasz 
mindig nagyobb vagy egyenlő 0-val, függetlenül attól, hogy a 
múltban volt vagy a jövőben.
*/
namespace _012_twice_as_old
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(TwiceAsOld(45,10));
        }

        public static int TwiceAsOld(int dadYears, int sonYears)
        {
            return dadYears - (sonYears * 2) < 0 ? (dadYears - (sonYears * 2)) * -1 : dadYears - (sonYears * 2);
        }

    }
}
