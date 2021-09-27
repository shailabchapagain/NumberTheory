from menu import *
from cipher import *
from sys import exit
import pyperclip

path = "text_to_encrypt.txt"
path2="text_to_decrypt.txt"

while True:

    clear()
    choice = menu()

    while choice not in range(0, 3):
        clear()
        print("\n !!! Invalid Choice please enter a number between 0 to 2 !!!\n")
        if choice == -1:
            print("\t\t  Number must be an integer\n")
        choice = menu()

    if choice == 1:
        clear()
        print("\tYou choose to ENCRYPT\n")
        subchoice = submenu()
        while subchoice not in range(0, 4):
            clear()
            print("\n !!! Invalid Choice please enter a number between 0 to 3 !!!\n")
            if subchoice == -1:
                print("\t\t  Number must be an integer\n")
            subchoice = submenu()

        if subchoice == 1:
            text_to_encrypt= str(input("Enter any Message: \n"))
            j = encrypt(text_to_encrypt)

        elif subchoice == 2:
            data = open(path, "r")
            f=data.read()
            encrypt(f)

        elif subchoice == 3:
            input("Please copy your text to encrypt to clipboard ... [Ctrl + C] ... then hit [ENTER]")
            f=pyperclip.paste()
            encrypt(f)


    elif choice == 2:
            clear()
            print("\tYou choose to DECRYPT.\n")
            subchoice = submenu()
            while subchoice not in range(0, 4):
                clear()
                print("\n !!! Invalid Choice please enter a number between 0 to 3 !!!\n")
                if subchoice == -1:
                    print("\t\t  Number must be an integer\n")
                subchoice = submenu()

            if subchoice == 1:
                text_to_decrypt= str(input("Enter the Message(If Possible,Please choose the output you got before): \n"))
                decrypt(text_to_decrypt)

            elif subchoice == 2:
                data = open(path2, "r")
                f=data.read()
                decrypt(f)

            elif subchoice == 3:
                input("Please copy your encrypted text to clipboard ... [Ctrl + C] ... then hit [ENTER]")
                f=pyperclip.paste()
                decrypt(f)

    print("\nPress ENTER to --GO TO MENU-- or 0 to exit\n")
    xchoice = input(".....Waiting for the Response.....\n")
    if xchoice == "0" :exitCheck(0)
