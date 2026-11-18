""" 1 = Stone
    2 = Paper
    3 = Scissor
"""
m = input("""Select the mode:
Endless or Best of 3
""").strip().lower()

if m not in ["endless", "best of 3"]:
    print("Invalid input")
    exit()

if m == "endless":

    us = 0
    os = 0

    def sps():
        global us, os

        import random

        c = random.choice(["stone", "paper", "scissor"])

        u = input("""Make your choice STONE, Paper or SCISSOR:
""").strip().lower()

        if u not in ["stone", "paper", "scissor"]:
            print("Invalid input")
            return

        print("You chose:", u)
        print("Your opponent chose:", c)

        if c == u:
            print("It's a DRAW")

        elif (c == "stone" and u == "paper") or \
             (c == "paper" and u == "scissor") or \
             (c == "scissor" and u == "stone"):

            print("Congrats, you WIN")
            us += 1

        else:
            print("Oops! you lose")
            os += 1

        print("Your score =", us)
        print("Opponent's score =", os)

    while True:

        sps()

        play = input("Play again? (Yes/NO): ").strip().lower()

        if play not in ["yes", "no"]:
            print("Invalid input")
            continue

        if play != "yes":
            print("THANKS for playing")
            break


else:

    us2 = 0
    os2 = 0
    w = 0
    l = 0

    def sps2():
        global us2, os2, w, l

        import random

        c2 = random.choice(["stone", "paper", "scissor"])

        u2 = input("""Make your choice
STONE, Paper or SCISSOR:
""").strip().lower()

        if u2 not in ["stone", "paper", "scissor"]:
            print("Invalid input")
            return

        print("You chose:", u2)
        print("Your opponent chose:", c2)

        if c2 == u2:
            print("It's a DRAW")

        elif (c2 == "stone" and u2 == "paper") or \
             (c2 == "paper" and u2 == "scissor") or \
             (c2 == "scissor" and u2 == "stone"):

            print("Congrats, you WIN")
            us2 += 1

        else:
            print("Oops! you lose")
            os2 += 1

        print("Your score =", us2)
        print("Opponent's score =", os2)

        if us2 >= 2:
            print("Congrats, you WIN")
            w += 1

        elif os2 >= 2:
            print("Oops! you LOST.....")
            l += 1

    while w < 1 and l < 1:
        sps2()

    print("THANKS for playing")