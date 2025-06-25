/*
Kódot írsz a városod közlekedési lámpáinak vezérléséhez. Szüksége van egy függvényre, 
amely kezeli a zöldről, sárgára, pirosra, majd ismét zöldre váltást.
Fejezze be a függvényt, amely egy karakterláncot vesz fel argumentumként, 
amely a fény aktuális állapotát reprezentálja, és egy karakterláncot ad vissza, 
amely azt az állapotot jelzi, amelyre a fénynek át kell váltania.
Például, ha a bemenet zöld, a kimenetnek sárga színűnek kell lennie.
*/

namespace Thinkful___Logic_Drills_Traffic_light
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
        public static string UpdateLight(string current)
        {
            switch (current)
            {
                case "green": return "yellow"; 
                case "yellow": return "red"; 
                case "red": return "green"; 
                default: return "Gáz vaan!";
                //nem kell break mert return-van a kiértékelés után
            }
        }
    }
}
