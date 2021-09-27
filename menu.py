from sys import exit
from os import system, name

o1 = "  1. Encrypt"
o2 = "  2. Decrypt"

o0 = "  0. Exit (Enter 0 in any field to exit)"

p1 = "  1. From Terminal"
p2 = "  2. From To File"
p3 = "  3. From Clipboard"

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def exitCheck(in_int):
    if in_int == 0:
        clear()
        print("\n         You chose to Exit                 \n")
        print("----Thank You ... Press [Enter to Exit]----\n")
        input()
        exit()


def menu():
    print("\t+" + "-" * 52 + "+")
    print("\t|   CRYPTOGRAPHY USING MOD OF TWO RANDOM NUMBERS   |")
    print("\t" + "+" + "-" * 52 + "+")
    print("\t|" + o1 + " " * (52 - len(o1)) + "|")
    print("\t|" + o2 + " " * (52 - len(o2)) + "|")
    print("\t|" + " " * 52 + "|")
    print("\t|" + o0 + " " * (52 - len(o0)) + "|")
    print("\t+" + "-" * 52 + "+")

    try:
        choice = int(input("\t   # Enter you choice : "))
        exitCheck(choice)
        return choice
    except ValueError:
        return -1

def submenu():
    print("\t+" + "-" * 52 + "+")
    print("\t| INPUT/OUTPUT SOURCE"+" "*(52-23)+"|")
    print("\t+" + "-" * 52 + "+")
    print("\t|" + p1 + " " * (52 - len(p1)) + "|")
    print("\t|" + p2 + " " * (52 - len(p2)) + "|")
    print("\t|" + p3 + " " * (52 - len(p3)) + "|")
    print("\t|" + " " * 52 + "|")
    print("\t|" + o0 + " " * (52 - len(o0)) + "|")
    print("\t+" + "-" * 52 + "+")

    try:
        subchoice = int(input("\t   # Enter you choice : "))
        exitCheck(subchoice)
        return subchoice
    except ValueError:
        return -1
