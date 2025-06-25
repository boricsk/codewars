/*
Adott egy tömb (arr) argumentumként fejezze be a countSmileys függvényt, amelynek vissza kell adnia a mosolygó arcok számát.

A mosolygó arc szabályai:

Minden mosolygós arcnak érvényes szempárt kell tartalmaznia. A szemek a következőképpen jelölhetők: vagy ;
A mosolygós arcnak lehet orra, de nem kell. Az orr érvényes karakterei a - vagy a ~
Minden mosolygó arcnak mosolygós szájjal kell rendelkeznie, amelyet ) vagy D betűvel kell megjelölni
További karakterek nem megengedettek, kivéve az említetteket.

Érvényes mosolygós példák: :) :D ;-D :~)
Érvénytelen mosolygó arcok: ;( :> :} :]

Példa 
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
*/
namespace _019_count_smiley
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] tests = { ":)", ";(", ";}", ":-D" };
            Console.WriteLine(CountSmileys(tests));
        }
        public static int CountSmileys(string[] smileys)
        {
            if (smileys.Count() == 0 || smileys == null) { return 0; }
            int count = 0;
            string[] valid_smiles = { ":)", ":-)", ":~)", ":D", ":-D", ":~D", ";)", ";-)", ";~)", ";D", ";-D", ";~D" };

            foreach (string smiley in smileys)
            {
                if (valid_smiles.Contains(smiley)) { count++; }
            }
            return count;
        }
    }
}
