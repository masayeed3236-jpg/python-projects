#number guessing game :

import random

print("WELCOME TO THE NUMBER GUESSING GAME ")

def num_game():
    secret_Num =random.randint(1,100)
    count=5
    

    while True:
        userInput=int(input("enter the number to guess "))
        if userInput==0:
            break

        if count==0:
            print(f"GAME OVER , please try again , the number was {secret_Num} :) :) ...... ! ")
            

        else :
            print(f"you have {count} left : ")
            count-=1

            if userInput<secret_Num:
                print(f"you have guessed {userInput} .... please increase your number ")

            elif userInput>secret_Num:
                print(f"you have guessed {userInput} .... please decrease your number ")

            elif userInput==secret_Num:
                print ("you have the guessed number :::congratulations:::  . .... ")
                break 

            else :
                print('GOOD KEEP PLAYING ')
                

                
num_game()
print("thanks for playing Number Guessing Game ")
