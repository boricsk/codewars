

using System.Collections;
using System.Diagnostics;

namespace _4By4Skyscrapers
{
    #region Data model
    public class Combination
    {
        public int[] line { get; set; } = new int[4];
        public int lineStartClue { get; set; }
        public int lineEndClue { get; set; }
    }
    #endregion

    #region Permutation helper
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
    #endregion

    internal class Program
    {
        static void Main(string[] args)
        {
            var clues = new[]{ 2, 2, 1, 3,
                               2, 2, 3, 1,
                               1, 2, 2, 3,
                               3, 2, 1, 3};

            var expected = new[]{  new []{1, 3, 4, 2},
                                   new []{4, 2, 1, 3},
                                   new []{3, 4, 2, 1},
                                   new []{2, 1, 3, 4 }};

            SolvePuzzle(clues);

        }

        public static int[][] SolvePuzzle(int[] clues)
        {
            var _combinations = GetCombinations();
            int[][] ret = new int[4][];

            //Előszűrés a sorokhoz
            List<Combination>[] possibleRows = new List<Combination>[4];

            for (int row = 0; row < 4; row++)
            {
                int leftClue = clues[15 - row];
                int rightClue = clues[4 + row];

                possibleRows[row] = _combinations
                    .Where(c =>
                        (leftClue == 0 || c.lineStartClue == leftClue) &&
                        (rightClue == 0 || c.lineEndClue == rightClue))
                    .ToList();
            }
            return FindValidGrid(possibleRows,clues); 
        }

        #region Backtrack search
        //Oszlopduplikáció ellenőrzés a backtrackhez
        private static bool HasNoColumnConflicts(List<int[]> currentRows, int rowIndex)
        {
            for (int col = 0; col < 4; col++)
            {
                var seen = new HashSet<int>();
                for (int row = 0; row <= rowIndex; row++)
                {
                    int value = currentRows[row][col];
                    if (seen.Contains(value))
                        return false;
                    seen.Add(value);
                }
            }
            return true;
        }
        //Főkeresés
        private static int[][] FindValidGrid(List<Combination>[] possibleRows, int[] clues)
        {
            var currentRows = new List<int[]>();
            return Search(0);

            int[][]? Search(int rowIndex)
            {
                if (rowIndex == 4)
                {
                    if (ValidateColumns(currentRows, clues))
                        return currentRows.ToArray();
                    return null;
                }

                foreach (var candidate in possibleRows[rowIndex])
                {
                    currentRows.Add(candidate.line);
                    if (HasNoColumnConflicts(currentRows, rowIndex))
                    {
                        var result = Search(rowIndex + 1);
                        if (result != null)
                            return result;
                    }
                    currentRows.RemoveAt(currentRows.Count - 1);
                }

                return null;
            }
        }
        //Clue ellenőrzés oszlopokra
        private static bool ValidateColumns(List<int[]> board, int[] clues)
        {
            for (int col = 0; col < 4; col++)
            {
                int[] column = new int[4];
                for (int row = 0; row < 4; row++)
                    column[row] = board[row][col];

                int topClue = clues[col];
                int bottomClue = clues[11 - col];

                var (top, bottom) = GetClueNums(column);

                if ((topClue != 0 && topClue != top) ||
                    (bottomClue != 0 && bottomClue != bottom))
                    return false;
            }

            return true;
        }
        #endregion
        
        #region Permutation
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
        #endregion
    }
}
