from random import randint

def gbb_game(you) :
    com = randint(1,3)
    if com - you == 1 or com - you == -2 :
        print("com 승")

    elif com == you :
        print('비김')

    else:
        print('you 승')

    print("com : %d " % com)

you = int(input("you 입력(1:가위, 2:바위, 3:보) : "))
gbb_game(you)

