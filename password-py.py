import random
import string

chars = string.printable
chars_list = list(chars)



password = str(input("Password : "))
guess_password = ""



while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("maching.."+str(guess_password))

    if(guess_password == list(password)):
        print("your password is : "+ "".join(guess_password))
        break