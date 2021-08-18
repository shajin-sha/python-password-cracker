from typing import Generator
import wordlist

password = str(input("Password :  "))

generator = wordlist.Generator(password)


for each in generator.generate(1,10):
    if each == password:
        break
    print(each)
        
        
    # if(each == password):
    #     break
    # print(each)
        