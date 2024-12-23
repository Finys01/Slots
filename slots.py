import random as rd
symbols = ["🥝","🍉","🍒","🍑","🍋"]
slot = []
win = 0
bet = 0
tokens = 1000
game= "y"
def check_win(symbol):
    return(
       (slot[0][0] == slot[0][1] == slot[0][2] == symbol or
        slot[1][0] == slot[1][1] == slot[1][2] == symbol or
        slot[2][0] == slot[2][1] == slot[2][2] == symbol or
        slot[0][0] == slot[1][1] == slot[2][2] == symbol or
        slot[2][0] == slot[1][1] == slot[0][2] == symbol))
print("Welcome to Filda slots")
print('\033[31m'+"To change bet write (b)"+'\033[0m')
while bet != 5  and bet != 10 and bet != 25 and bet != 50 and bet != 100:
    bet = int(input("Choose bet (5,10,25,50,100): "))
while game != "n":
    if game == "b":
        bet = 0
        while bet != 5  and bet != 10 and bet != 25 and bet != 50 and bet != 100:
            bet = int(input("Choose bet (5,10,25,50,100): "))
    tokens = tokens - bet
    for i in range(1,4):
        slot_row = []
        for j in range(1,4):
            pick = rd.choice(symbols)
            slot_row.append(pick)
        print(slot_row)
        slot.append(slot_row)
    print(tokens)
    if check_win("🥝"):
        win = 1
    if check_win("🍉"):
        win = 2
    if check_win("🍒"):
        win = 3
    if check_win("🍑"):
        win = 4
    if check_win("🍋"):
        win = 5
    if win == 1 or win == 2 or win == 3 or win == 4 or win == 5:
        tokens += bet*5
        print("You win!")
        print(tokens)
    if tokens == 0:
        break
    game = input("Another game?(y/n/b) ")
    slot = []
    win = 0


