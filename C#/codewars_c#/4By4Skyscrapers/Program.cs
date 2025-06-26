

using System.Collections;
using System.Diagnostics;

namespace _4By4Skyscrapers
{
    public class Combination
    {
        public int[] line { get; set; } = new int[4];
        public int lineStartClue { get; set; }
        public int lineEndClue { get; set; }


    }
    public class PermutationHelper
    {
        public static List<int[]> GetAllPermutations(int[] array)
        {
            var result = new List<int[]>();
            Permute(array, 0, result);
            return result;
        }

        private static void Permute(int[] array, int start, List<int[]> result)
        {
            if (start == array.Length)
            {
                result.Add((int[])array.Clone());
            }
            else
            {
                for (int i = start; i < array.Length; i++)
                {
                    Swap(ref array[start], ref array[i]);
                    Permute(array, start + 1, result);
                    Swap(ref array[start], ref array[i]);
                }
            }
        }

        private static void Swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var clues = new[]{ 2, 2, 1, 3,
                               2, 2, 3, 1,
                               1, 2, 2, 3,
                               3, 2, 1, 3};

            var expected = new[]{ new []{1, 3, 4, 2},
                                   new []{4, 2, 1, 3},
                                   new []{3, 4, 2, 1},
                                   new []{2, 1, 3, 4 }};

            Console.WriteLine(SolvePuzzle(clues));

        }

        public static int[][] SolvePuzzle(int[] clues)
        {
            var _combinations = GetCombinations();
            int[][] ret = new int[4][];

            return ret;
        }
        private static List<Combination> GetCombinations()
        {
            var ret = new List<Combination>();
            var allPermutations = PermutationHelper.GetAllPermutations(new[] { 1, 2, 3, 4 });

            foreach (var perm in allPermutations)
            {
                ret.Add(new Combination()
                {
                    line = perm,
                    lineStartClue = GetClueNums(perm).start,
                    lineEndClue = GetClueNums(perm).end,
                });
            }
            return ret;
        }

        private static (int start, int end) GetClueNums(int[] pLineArray)
        {
            var ret = (0, 0);
            int maxHeight = 0;
            foreach (int height in pLineArray)
            {
                if (height > maxHeight)
                { 
                    maxHeight = height;
                    ret.Item1++;
                }
            }
            maxHeight = 0;
            foreach (int height in pLineArray.Reverse())
            {
                if (height > maxHeight)
                {
                    maxHeight = height;
                    ret.Item2++;
                }
            }

            return ret;
        }
    }
}
