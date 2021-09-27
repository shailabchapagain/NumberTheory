from myfunc import modular as mod
from myfunc import gcd
from random import randint as ran
import pyperclip


def encrypt(tx):
    print("Your original text is: \n",tx)
    w = ran(1,99)
    x = ran(1,99)
    y = ran(1,99)
    z = ran(1,99)
    a = gcd(w,x)
    b= gcd(y,z)
    y= ""
    for ch in tx:
        y = y + str((ord(ch) + mod(a,b)))+","
    y = y+str(a)+","+str(b)
    print("\nYour Encrypted text is: \n",y)

    #write to a file
    data = open("encrypted.txt", "w")
    data.write(y)
    print("\nThe encrypted text has been written to encrypted.txt successfully")

    #copy to cp
    pyperclip.copy(y)
    print("Your encrypted text has been copied to clipboard successfully\n")
    return y


def decrypt(text):
    print("Your entered message was: \n" + text)
    tsplit =  text.split(',')
    try:
        a = tsplit[-2]
        a = int(a)
        b = tsplit[-1]
        b = int(b)
        txtsplit = tsplit[:-2]
    except:
        print("\n !!! Please use text encrypted by our program !!!\n")
        return "ERROR"

    y=""
    for ch in txtsplit:
        try:
            c = int(ch)
        except:
            print("Please use text encrypted by our program")
            return "ERROR"
        y = y + chr(c - mod(a,b))

    print("\nYour decrypted message is: \n",y)

    #write to a file
    data = open("decrypted.txt", "w")
    data.write(y)
    print("\nThe decrypted text has been written to decrypted.txt successfully")

    #copy to cp
    pyperclip.copy(y)
    print("Your decrypted text has been copied to clipboard successfully\n")

    return y
