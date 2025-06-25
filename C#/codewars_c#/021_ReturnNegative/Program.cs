namespace _021_ReturnNegative
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(MakeNegative(-3));
        }

        public static int MakeNegative(int number)
        {            
            //return int.IsNegative(number) ? number : number * -1;
            //Negálunk minden bitet és 1-et hozzáadunk.
            return int.IsNegative(number) ? number : ~number + 1;
        }
    }
}
