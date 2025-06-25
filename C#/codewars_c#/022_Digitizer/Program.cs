namespace _022_Digitizer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Digitize(3654);
        }

        public static long[] Digitize(long n)
        {
            long[] ns = n.ToString().Select(c => (long)(c - '0')).Reverse().ToArray();
            return ns;
        }
    }
}
