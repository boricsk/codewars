namespace Pract_StringOperations
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string test = "Alma4fa7dolog987";
            M1(test); Console.WriteLine();
            M2(test); Console.WriteLine();
            M3(test); Console.WriteLine();
            M4("vakáció"); Console.WriteLine();
            M31("Minden magánhangzó megduplázása"); Console.WriteLine();
            M32("Minden magánhangzó megduplázása"); Console.WriteLine();
            M41("magánhangzók cseréje *karakterre"); Console.WriteLine();
            M5("tetszőleges szövegrészlet kivágása (X.helytől Y hosszon) saját eljárással, hibás x és y esetén hibaüzenettel", 7, 12); Console.WriteLine();
            M6("szöveg titkosítása: minden karakterhez hozzá adunk ASCII szerint X értéket (X=1 - nél a helyett b, b helyett c stb.", 13); Console.WriteLine();
            M7("minden 2.és 3.betű új szövegbe"); Console.WriteLine();
            M7("szóközök kicserélés _ jelre"); Console.WriteLine();
            M9("minden karakter megkettőzése: abc->aabbcc"); Console.WriteLine();
            M10("minden 3.és 5.betű cseréje * -ra"); Console.WriteLine();
            M12("hullámos szöveg (pl. alma -> AlMa)"); Console.WriteLine();
            M13("páros és páratlan betűk cseréje(abcd->badc)"); Console.WriteLine();
            M14("m1nden 5zámjegy megdup1ázása"); Console.WriteLine();
            M15("magánhangzók cseréje nagybetűsre(pl.abcde->AbcdE)"); Console.WriteLine();
            M16("Ékezettelenítés űber ökör kóborol a mezŐn"); Console.WriteLine();
            M18("magánhangzók megszámlálása (angol abc)"); Console.WriteLine();
            M19("élefazssiv gevözs"); Console.WriteLine();
            M20("minden mássalhangzó megduplázása"); Console.WriteLine();
            M21("21 számok kiválogatása szövegből(pl.a1b2c3-> 123)"); Console.WriteLine();
        }

        static void M1(string s)
        {
            //1 számjegyek cseréje úgy, hogy az eredeti számhoz adva 9-et kapjunk (pl. 1->8; 5->4; 0->9...)
            for (int i = 0; i < s.Length; i++)
            {
                switch (s[i])
                {
                    case '0': Console.Write("9"); break;
                    case '1': Console.Write("8"); break;
                    case '2': Console.Write("7"); break;
                    case '3': Console.Write("6"); break;
                    case '4': Console.Write("5"); break;
                    case '5': Console.Write("4"); break;
                    case '6': Console.Write("3"); break;
                    case '7': Console.Write("2"); break;
                    case '8': Console.Write("1"); break;
                    case '9': Console.Write("0"); break;
                    default:
                        Console.Write(s[i]); break;

                }
            }
        }

        static void M2(string s)
        {
            //M1 másik megoldása
            for (int i = 0; i < s.Length; i++)
            {
                switch (s[i])
                {
                    case '0': //ASCII 48
                    case '1':
                    case '2':
                    case '3':
                    case '4':
                    case '5':
                    case '6':
                    case '7':
                    case '8':
                    case '9': Console.Write((char)57 - s[i]); break;
                    default:
                        Console.Write(s[i]); break;

                }
            }
        }
        static void M3(string s)
        {
            //M1 harmadik megoldása
            for (int i = 0; i < s.Length; i++)
            {
                if ((char)s[i] >= 48 & (char)s[i] <= 57)
                {
                    Console.Write((char)57 - s[i]);
                }
                else
                {
                    Console.Write(s[i]);
                }
            }
        }
        static void M4(string s)
        {
            //ó, ió, ció, áció

            for (int i = s.Length; i > 0; i--)
            {
                Console.WriteLine(s.Substring(s.Length - i));
            }

            for (int i = 0; i <= s.Length; i++)
            {
                Console.WriteLine(s.Substring(s.Length - i));
            }
        }
        static void M31(string s)
        {
            //minden magánhangzó megduplázása
            string maganhangzó = "aáeéiíoóöőuúüű";
            for (int i = 0; i < s.Length; i++)
            {
                for (int j = 0; j < maganhangzó.Length; j++)
                {
                    if (s[i] == maganhangzó[j])
                    {
                        Console.Write(s[i]);
                    }
                    else { }
                }
                Console.Write(s[i]);
            }
        }
        static void M32(string s)
        {
            char[] maganhangzó = { 'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű' };
            for (int i = 0; i < s.Length; i++)
            {
                if (maganhangzó.Contains(s[i]))
                {
                    Console.Write($"{s[i]}{s[i]}");
                }
                else { Console.Write(s[i]); }
            }
        }

        static void M41(string s)
        {
            //4 magánhangzók cseréje *karakterre
            char[] maganhangzó = { 'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű' };
            for (int i = 0; i < s.Length; i++)
            {
                if (maganhangzó.Contains(s[i]))
                {
                    Console.Write("*");
                }
                else { Console.Write(s[i]); }
            }
        }

        static void M5(string s, int start, int end)
        {
            //5 tetszőleges szövegrészlet kivágása (X.helytől Y hosszon) saját eljárással, hibás x és y esetén hibaüzenettel
            if (start > s.Length) { Console.WriteLine("A kezdő pozíció nagyobb mint a string hossza"); }
            else if (start + end > s.Length) { Console.WriteLine("Hibás hossz"); }
            else
            {
                for (int i = start; i < start + end; i++)
                {
                    Console.Write(s[i]);
                }
            }

        }
        static void M6(string s, int eltolas)
        {
            for (int i = 0; i < s.Length; i++)
            {
                Console.Write((char)(s[i] + eltolas));
            }
        }
        static void M7(string s)
        {
            Console.WriteLine(s);
            string newText = string.Empty;

            for (int i = 0; i < s.Length; i++)
            {
                if (((i + 1) % 2 == 0) | ((i + 1) % 3 == 0)) { newText += s[i]; }
            }
            Console.WriteLine(newText);
        }
        static void M8(string s)
        {
            for (int i = 0; i < s.Length; i++)
            {
                if ((char)s[i] == 32) { Console.Write("_"); } else { Console.Write(s[i]); }
            }
        }

        static void M9(string s)
        {
            for (int i = 0; i < s.Length; i++)
            {
                Console.Write($"{s[i]}{s[i]}");
            }
        }

        static void M10(string s)
        {
            for (int i = 0; i < s.Length; i++)
            {
                if (((i + 1) % 3 == 0) | ((i + 1) % 5 == 0)) { Console.Write("*"); } else { Console.Write(s[i]); }
            }
        }

        static void M12(string s)
        {
            for (int i = 0; i < s.Length; i++)
            {
                if (i % 2 == 0) { Console.Write(char.ToUpper(s[i])); } else { Console.Write(s[i]); }
            }
        }

        static void M13(string s)
        {
            Console.Write($"{s[0]}{s[1]}");

            for (int i = 2; i < s.Length - 1; i += 2)
            {
                Console.Write($"{s[i + 1]}{s[i]}");
            }
        }

        static void M14(string s)
        {
            for (int i = 0; i < s.Length; i++)
            {
                if (char.IsDigit(s[i]))
                {
                    Console.Write($"{s[i]}{s[i]}");
                }
                else
                {
                    {
                        Console.Write(s[i]);
                    }
                }
            }
        }

        static void M15(string s)
        {
            char[] maganhangzó = { 'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű' };
            for (int i = 0; i < s.Length; i++)
            {
                if (maganhangzó.Contains(s[i]))
                {
                    Console.Write(char.ToUpper(s[i]));
                }
                else { Console.Write(s[i]); }
            }
        }

        static void M16(string s)
        {
            char[] ekezet = { 'á', 'Á', 'é', 'É', 'ő', 'Ő', 'ó', 'Ó', 'ü', 'Ü', 'ú', 'Ú', 'ű', 'Ű', 'í', 'Í', 'ö', 'Ö' };
            char[] sima = { 'a', 'A', 'e', 'e', 'o', 'O', 'o', 'O', 'u', 'U', 'u', 'U', 'u', 'U', 'i', 'I', 'o', 'O' };
            int position = 0;

            for (int i = 0; i < s.Length; i++)
            {
                if (ekezet.Contains(s[i]))
                {
                    position = 0;
                    foreach (char c in ekezet)
                    {
                        if (c == s[i])
                        {
                            Console.Write(sima[position]);
                        }
                        position++;
                    }
                }
                else
                {
                    Console.Write(s[i]);
                }
            }
        }

        static void M18(string s)
        {
            char[] maganhangzok = { 'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u' };
            int count = 0;
            for (int i = 0; i < s.Length; i++)
            {
                if (maganhangzok.Contains(s[i]))
                {
                    count++;
                }
            }
            Console.WriteLine($"A magánhangzók száma : {count} a következő szövegben : {s}");
        }

        static void M19(string s)
        {
            for (int i = s.Length - 1; i >= 0; i--)
            {
                Console.Write(s[i]);
            }
        }

        static void M20(string s)
        {
            char[] maganhangzok = { 'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u' };
            for (int i = 0; i < s.Length; i++)
            {
                if (maganhangzok.Contains(s[i]))
                {
                    Console.Write(s[i]);
                }
                else
                {
                    Console.Write($"{s[i]}{s[i]}");
                }
            }
        }

        static void M21(string s)
        {
            string result = "";
            for (int i = 0; i < s.Length; i++)
            {
                if (char.IsDigit(s[i]))
                {
                    result += s[i];
                }
            }
            Console.WriteLine(result);
        }
    }
}
