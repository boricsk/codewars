namespace _011_invert_value
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] test = { 1, 2, 3 };
            foreach (int i in InvertValues(test))
            {
                Console.WriteLine(i);
            }
        }
        public static int[] InvertValues(int[] input)
        {
            int[] result = new int[input.Length];
            for (int i  = 0; i < input.Length;i++)
            {
                result[i] = input[i] * -1;
            }
            return result;
            //Code it!
        }
    }
}
