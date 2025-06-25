"""
https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c/train/python

Kate folyamatosan valamilyen útvesztőben találja magát. Segíts neki megtalálni 
a kiutat!

Adott labirintusra és Kate helyzetére keresse meg, van-e kiút. A függvénynek 
igaz vagy hamis értéket kell adnia.

Minden labirintus karakterláncok listájaként van meghatározva, ahol minden 
karakter egyetlen labirintus "cellában" marad. A ' ' (szóköz) ráléphet, 
a '#' a falat jelenti, a 'k' pedig Kate kiindulási pozícióját jelenti. 
Vegye figyelembe, hogy a labirintus nem mindig négyzet vagy akár téglalap alakú.

Kate csak balra, fel, jobbra vagy le tud mozogni.

Csak 1 Kate lehet bent, ha több van akkor kivételt kell generálni.

def basic_test_cases():
        maze = ["k"]
        test.assert_equals(has_exit(maze), True, "simplest case")

        maze = ["###",
                "#k#",
                "###"]
        test.assert_equals(has_exit(maze), False, "no exit case")

        maze = ["###",
                "#k ",
                "###"]
        test.assert_equals(has_exit(maze), True, "single exit case")

        maze = ["k ",
                "kk"]

        test.expect_error("There should no be multiple Kates", lambda: has_exit(maze))

    @test.it("More difficult cases")
    def basic_test_cases():

        maze = ["########",
                "# # ####",
                "# #k#   ",
                "# # # ##",
                "# # # ##",
                "#      #",
                "########"]
        test.assert_equals(has_exit(maze), True, "single exit big maze")

        maze = ["########",
                "# # ## #",
                "# #k#  #",
                "# # # ##",
                "# # #  #",
                "#     ##",
                "########"]
        test.assert_equals(has_exit(maze), False, "no exit big maze")
"""

maze1 = ["k ",
        "kk"]

def has_exit(maze):
    ret = False
    num_of_kate = 0
    for i in maze:
        for j in i:
            if j == 'k':
                num_of_kate += 1
            
    return num_of_kate    

print(has_exit(maze1))