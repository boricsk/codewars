namespace _010_string_repeat
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
        public static string RepeatStr(int n, string s)
        {
            string ret = "";
            for (int i = 0; i < n; i++)
            {
                ret += s;
            }
            return ret;
        }
    }
}
