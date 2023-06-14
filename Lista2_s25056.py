#Zadanie 1
a1 = int(input("podaj poczatkowa liczbe: "))
b1 = int(input("podaj koncowa liczbe: "))
c1 = int(input("podaj odstep: "))
for i in range(a1, b1 +1, c1):
    print(i, end = "\n")

#Zadanie 2

str1 = input("Podaj napis: ")
print(str1[::-1])

#Zadanie 3
import random

slowa = ['piotr', 'balcer', 'krzeslo', 'informatyka', 'selekcja']
wylosowaneSlowo = random.choice(slowa)
print("Wylosowane słowo ma", len(wylosowaneSlowo), "liter.")

for i in range(5):
    litera = input("Wprowadz litere ").lower()
    if litera == wylosowaneSlowo:
        print("odgadłeś słowo!")
        break
    if litera in wylosowaneSlowo:
        print("Ta litera znajduje się w słowie")
    else:
        print("Ta litera nie znajduje się w słowie")

    if i == 4:
        slowo = input("ostatnia szansa : ").lower()
        if slowo == wylosowaneSlowo:
            print("odgadłeś słowo!")
            break
        else:
            print("nie udało ci się odgadnąć . Szukane słowo:", wylosowaneSlowo)
            break


#Zadanie 4
import random

words_list = ['piotr', 'balcer', 'krzeslo', 'informatyka', 'selekcja']
word = random.choice(words_list)
str2 = ''
szansy = 10

while szansy > 0:
    failed = 0
    for char in word:
        if char in str2:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nWygrałeś!")
        break
    print("\nPozostało Ci", szansy, "szans.")
    guess = input("Zgadnij literę: ")
    str2 += guess
    if guess not in word:
        szansy -= 1
        print("Nie ma takiej litery.")
        if szansy == 0:
            print("Przegrałeś! Szukane słowo to", word)

#Zadanie 5
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = "X"

def draw_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def make_move():
    global current_player
    position = int(input("Gracz " + current_player + ", podaj pozycję (1-9): ")) - 1
    if board[position] != "X" and board[position] != "O":
        board[position] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        print("To pole jest już zajęte! Wybierz inne pole.")

def check_winner():
    winner = None
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    cols = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    diags = [[0, 4, 8], [2, 4, 6]]
    lines = rows + cols + diags
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            winner = board[line[0]]
            break
    return winner


def is_board_full():
    ilosc = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    flag = True
    for i in range(9):
        if board[i] in ilosc:
            flag = False
    return flag

draw_board()
while True:
    make_move()
    draw_board()
    winner = check_winner()
    if winner:
        print("Gracz " + winner + " wygrał!")
        break
    if is_board_full():
        print("Remis!")
        break


