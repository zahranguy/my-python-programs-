endGame = False
turn = "X"
var = 0
won = False
# the board!!!!!
print("""    1|2|3
   --+-+--
    4|5|6
   --+-+--
    7|8|9 """)
a = """     | | 
   --+-+--
     | | 
   --+-+--
     | | """

# so i dont have to type all that
def changechar(lst, chr):
    global a
    global var
    text = list(a)
    text[lst] = chr
    a = "".join(text)
    print(a)
def checkchar(lst):
    global a
    txt = list(a)
    if txt[lst] == "X":
        global var
        var = 1
    elif txt[lst] == "O":
        var = 1
    else:
        var = 0
    if var == 1:
        print("that spot is taken")
        global turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        return True
#where it gets replaced
while endGame == False:
    pos = input("where do you want to go? current turn: " + turn + "  ")
    if pos not in ["1","2","3","4","5","6","7","8","9"]:
        print("1-9 only")
        continue
    if pos == "1" and checkchar(4) is not True:
        changechar(4, turn)
    elif pos == "2" and checkchar(6) is not True:
        changechar(6, turn)
    elif pos == "3" and checkchar(8) is not True:
        changechar(8, turn)
    elif pos == "4" and checkchar(25) is not True:
        changechar(25, turn)
    elif pos == "5" and checkchar(27) is not True:
        changechar(27, turn)
    elif pos == "6" and checkchar(29) is not True:
        changechar(29, turn)
    elif pos == "7" and checkchar(46) is not True:
        changechar(46, turn)
    elif pos == "8" and checkchar(48) is not True:
        changechar(48, turn)
    elif pos == "9" and checkchar(50) is not True:
        changechar(50, turn)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    #winner winner
    if (a[4] == a[6] == a[8] == "O" or a[25] == a[27] == a[29] == "O" or a[46] == a[48] == a[50] == "O" or
        a[4] == a[25] == a[46] == "O" or a[6] == a[27] == a[48] == "O" or a[8] == a[29] == a[50] == "O" or
        a[4] == a[27] == a[50] == "O" or a[8] == a[27] == a[46] == "O"):
        print("O wins")
        endGame = True
        won = True
    if (a[4] == a[6] == a[8] == "X" or a[25] == a[27] == a[29] == "X" or a[46] == a[48] == a[50] == "X" or
        a[4] == a[25] == a[46] == "X" or a[6] == a[27] == a[48] == "X" or a[8] == a[29] == a[50] == "X" or
        a[4] == a[27] == a[50] == "X" or a[8] == a[27] == a[46] == "X"):
        print("X wins")
        endGame = True
        won = True
    if (a[4] != " " and a[6] != " " and a[8] != " " and
        a[25] != " " and a[27] != " " and a[29] != " " and
        a[46] != " " and a[48] != " " and a[50] != " ") and won == False:
        print("tie")
        endGame = True
exit()