namespace _013_count_sheeps
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
        public static int CountSheeps(bool[] sheeps)
        {
            int count = 0;
            for (int i = 0; i < sheeps.Length; i++) 
            {
                if (sheeps[i]) { count++; }
            }
            return count;
        }
    }
}
