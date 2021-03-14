import math


def decryption():
    print("\nEnter the text to be solved as a file.\n"
          "You must press to 1 for starting.")
    text_in = int(input(">>"))

    if text_in == 1:
        full_lock = []
        try:
            with open(input("Enter the file name with extension.\n>>"), "r") as f:
                for line in f:
                    full_lock.append(line.strip())

        except:
            print("The file not found! \n"
                  "Please, check the name of the file and try again.\n"
                  "The file must be in the folder where you run the program. ")
            decryption()

        print(full_lock)
        decryptions = []

        for i in full_lock:
            decryptions.append(int(i))

    decryption_0 = []

    for i in decryptions:
        decryption_0.append(int(i))


    n = int(input("Enter a key value \n: "))
    key = [(n // (10 ** i)) % 10 for i in range(math.ceil(math.log(n, 10)) - 1, -1, -1)]

    sum = 0

    for i in key:
        sum = sum + i

    print(sum)

    decryption_1 = []

    for i in decryption_0:
        if i%sum == 0:
            i = i/sum
            decryption_1.append(i)

        else:
            print("The wrong key or the wrong encrypted message was entered! "
                  "\nThe key entered with the message doesn't match. "
                  "\nPlease try again!")
            decryption()

    decryption_2 = []

    for i in decryption_1:

        if i == 16:
            i = "a"
            decryption_2.append(i)

        if i == 14:
            i = "b"
            decryption_2.append(i)

        if i == 21:
            i = "c"
            decryption_2.append(i)

        if i == 57:
            i = "ç"
            decryption_2.append(i)

        if i == 8:
            i = "d"
            decryption_2.append(i)

        if i == 47:
            i = "e"
            decryption_2.append(i)

        if i == 10:
            i = "f"
            decryption_2.append(i)

        if i == 39:
            i = "g"
            decryption_2.append(i)

        if i == 25:
            i = "ğ"
            decryption_2.append(i)

        if i == 5:
            i = "h"
            decryption_2.append(i)

        if i == 74:
            i = "ı"
            decryption_2.append(i)

        if i == 2:
            i = "i"
            decryption_2.append(i)

        if i == 66:
            i = "j"
            decryption_2.append(i)

        if i == 4:
            i = "k"
            decryption_2.append(i)

        if i == 55:
            i = "l"
            decryption_2.append(i)

        if i == 7:
            i = "m"
            decryption_2.append(i)

        if i == 63:
            i = "n"
            decryption_2.append(i)

        if i == 36:
            i = "o"
            decryption_2.append(i)

        if i == 72:
            i = "ö"
            decryption_2.append(i)

        if i == 18:
            i = "p"
            decryption_2.append(i)

        if i == 1:
            i = "r"
            decryption_2.append(i)

        if i == 99:
            i = "s"
            decryption_2.append(i)

        if i == 46:
            i = "ş"
            decryption_2.append(i)

        if i == 53:
            i = "t"
            decryption_2.append(i)

        if i == 48:
            i = "u"
            decryption_2.append(i)

        if i == 49:
            i = "ü"
            decryption_2.append(i)

        if i == 54:
            i = "v"
            decryption_2.append(i)

        if i == 56:
            i = "y"
            decryption_2.append(i)

        if i == 52:
            i = "z"
            decryption_2.append(i)

        if i == 58:
            i = "x"
            decryption_2.append(i)

        if i == 59:
            i = "q"
            decryption_2.append(i)

        if i == 28:
            i = "w"
            decryption_2.append(i)

        if i == 37:
            i = "."
            decryption_2.append(i)

        if i == 38:
            i = ","
            decryption_2.append(i)

        if i == 31:
            i = "!"
            decryption_2.append(i)

        if i == 30:
            i = "?"
            decryption_2.append(i)

        if i == 88:
            i = ")"
            decryption_2.append(i)

        if i == 71:
            i = "("
            decryption_2.append(i)

        if i == 20:
            i = ":"
            decryption_2.append(i)

        if i == 22:
            i = ";"
            decryption_2.append(i)

        if i == 81:
            i = "0"
            decryption_2.append(i)

        if i == 77:
            i = "1"
            decryption_2.append(i)

        if i == 83:
            i = "2"
            decryption_2.append(i)

        if i == 69:
            i = "3"
            decryption_2.append(i)

        if i == 93:
            i = "4"
            decryption_2.append(i)

        if i == 32:
            i = "5"
            decryption_2.append(i)

        if i == 64:
            i = "6"

            decryption_2.append(i)
        if i == 82:
            i = "7"
            decryption_2.append(i)

        if i == 9:
            i = "8"
            decryption_2.append(i)

        if i == 79:
            i = "9"
            decryption_2.append(i)

        if i == 100:
            i = " "
            decryption_2.append(i)

    solve = "".join(decryption_2)

    for i in range(2): print("~"*150)
    print(solve)
    for i in range(2): print("~"*150)

decryption()
