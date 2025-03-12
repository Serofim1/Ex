import random

slova = ["змея", "волк", "лиса", "заяц", "медведь"]
word = random.choice(slova)

def hangman(word):
    # wrong - отслеживание неправельных предположений
    wrong = 0
    stages = ["         ",
              "________ ",
              "|        ",
              "|   |    ",
              "|   0    ",
              "|  /|\   ",
              "|  / \   ",
              "|        "]
    # rlettes - список, содержащий каждый символ в переменной word
    # она же отслеживает какие буквы осталось отгадать
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пажаловать на казнь!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cing = rletters.index(char)
            board[cing] = char
            rletters[cing] = '$'
            print((" ".join(board)))
        else:
            wrong += 1
            print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выиграли! Было загадоно слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))

hangman(word)


    
