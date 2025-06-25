/*
Egy gyárban a nyomtató címkéket nyomtat a dobozokhoz. Az egyik típusú 
dobozhoz a nyomtatónak színeket kell használnia, amelyeket az 
egyszerűség kedvéért a-tól m-ig betűkkel nevezünk el.

A nyomtató által használt színek egy vezérlőkarakterláncban vannak rögzítve. 
Például egy 'jó' vezérlőkarakter aaabbbbhaijjjm, ami azt jelenti, hogy a 
nyomtató háromszor a színt, négyszer a b színt, egyszer a h színt, majd 
egyszer a színt használt...

Néha előfordulnak problémák: színhiány, műszaki hiba és 'rossz' vezérlősor 
keletkezik pl. aaaxbbbbyyhwawiwjjjwwm betűkkel nem a-tól m-ig.

Írnunk kell egy nyomtató_hiba függvényt, amely adott karakterlánccal 
visszaadja a nyomtató hibaarányát egy racionális karakterláncként, amelynek 
számlálója a hibák száma, nevezője pedig a vezérlőkarakterlánc hossza. 
Ne csökkentse ezt a törtet egyszerűbb kifejezésre.

A karakterlánc hossza egynél nagyobb vagy egyenlő, és csak a-tól z-ig terjedő betűket tartalmaz.

Példák: 

s='aaabbbbhaijjjm'
printer_error(s) => '0/14'

s='aaaxbbbbyyhwawiwjjjwwm'
printer_error(s) => '8/22'

*/
namespace _017_Printer_errors
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(PrinterError("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"));
        }

        public static string PrinterError(String s)
        {
            int err_count = 0;
            char[] colors = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' };
            s = s.ToUpper();
            int len = s.Length;
            string ret = "";

            for (int i = 0; i < s.Length; i++)
            {
                if (!colors.Contains(s[i])) { err_count++; }
            }

            return string.Concat(err_count.ToString(), "/", len.ToString());

        }
    }
}
