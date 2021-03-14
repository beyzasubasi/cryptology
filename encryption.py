import math
import random


def encryption():
    try:
        n = int(input("Enter a key value\n: "))

    except:
        print("The key must a numerical value! Please try again..\n>> ")
        encryption()

    if n == 0 or n == 1:
        print("The key can't be zero(0) or one(1). Please try again by entering a different key!\n>> ")
        encryption()

    else:
        key = [(n // (10 ** i)) % 10 for i in range(math.ceil(math.log(n, 10)) - 1, -1, -1)]

    sum = 0
    for i in key:
        sum = sum + i   #anahtar değerimin toplamını alıyorum

    print(sum)

    text = str(input("Please enter the text you want to encrypt. \n>> "))
    text = text.lower()

    letters = [c for c in text]  # içindeki kelimeyi harflere böldüm boşluklar dahil oü

    password = []

    for i in letters:

        if i == "a" or i == "â":
            i = 16
            password.append(i)

        elif i == "b":
            i = 14
            password.append(i)

        elif i == "c":
            i = 21
            password.append(i)

        elif i == "ç":
            i = 57
            password.append(i)

        elif i == "d":
            i = 8
            password.append(i)

        elif i == "e":
            i = 47
            password.append(i)

        elif i == "f":
            i = 10
            password.append(i)

        elif i == "g":
            i = 39
            password.append(i)

        elif i == "ğ":
            i = 25
            password.append(i)

        elif i == "h":
            i = 5
            password.append(i)

        elif i == "ı":
            i = 74
            password.append(i)

        elif i == "i":
            i = 2
            password.append(i)

        elif i == "j":
            i = 66
            password.append(i)

        elif i == "k":
            i = 4
            password.append(i)

        elif i == "l":
            i = 55
            password.append(i)

        elif i == "m":
            i = 7
            password.append(i)

        elif i == "n":
            i = 63
            password.append(i)

        elif i == "o":
            i = 36
            password.append(i)

        elif i == "ö":
            i = 72
            password.append(i)

        elif i == "p":
            i = 18
            password.append(i)

        elif i == "r":
            i = 1
            password.append(i)

        elif i == "s":
            i = 99
            password.append(i)

        elif i == "ş":
            i = 46
            password.append(i)

        elif i == "t":
            i = 53
            password.append(i)

        elif i == "u":
            i = 48
            password.append(i)

        elif i == "ü":
            i = 49
            password.append(i)

        elif i == "v":
            i = 54
            password.append(i)

        elif i == "y":
            i = 56
            password.append(i)

        elif i == "z":
            i = 52
            password.append(i)

        elif i == "x":
            i = 58
            password.append(i)

        elif i == "q":
            i = 59
            password.append(i)

        elif i == "w":
            i = 28
            password.append(i)

        elif i == ".":
            i = 37
            password.append(i)

        elif i == ",":
            i = 38
            password.append(i)

        elif i == "!":
            i = 31
            password.append(i)

        elif i == "?":
            i = 30
            password.append(i)

        elif i == ")":
            i = 88
            password.append(i)

        elif i == "(":
            i = 71
            password.append(i)

        elif i == ":":
            i = 20
            password.append(i)

        elif i == ";":
            i = 22
            password.append(i)

        elif i == "0":
            i = 81
            password.append(i)

        elif i == "1":
            i = 77
            password.append(i)

        elif i == "2":
            i = 83
            password.append(i)

        elif i == "3":
            i = 69
            password.append(i)

        elif i == "4":
            i = 93
            password.append(i)

        elif i == "5":
            i = 32
            password.append(i)

        elif i == "6":
            i = 64

            password.append(i)
        elif i == "7":
            i = 82
            password.append(i)

        elif i == "8":
            i = 9
            password.append(i)

        elif i == "9":
            i = 79
            password.append(i)

        elif i == " ":
            i = 100
            password.append(i)

    full_lock = []

    for i in password:    #anahtar değeriYLE her harfin değerini çarptım bu bana şifreyi verecektir
        i = i * sum
        full_lock.append(i)

    x = str(random.randrange(1, 10000))     #dosya adını random atıyorum

    print("\n\nName of The File: " + x + ".txt'dir.\n\n")

    with open("%s.txt" % x, "w")as f:
        for item in full_lock:
            f.write("%s\n" % item)

    print("The file saved successfully.")

    for i in range(2): print("x" * 150)
    print(full_lock)
    for i in range(2): print("x" * 150)


encryption()
