# Guess The number game
import random

print("===== Guess The Number Game ======")
print("==================================")

def generating_random ():
    num = random.randint(1, 51)
    return num

def game ():
    counter = 0
    GuessedNum = int(input("Please Guess number between 1 and 50 : "))
    CorrectNum = generating_random()
    while GuessedNum != CorrectNum :
        counter += 1
        if GuessedNum < CorrectNum :
            print("The right number is bigger than your guess ")
        elif GuessedNum > CorrectNum:
            print("The right number is smaller than your guess ")
        GuessedNum = int(input("Please Guess number between 1 and 50 : "))
    else:
        counter += 1
        print("YOU DID IT !!!!")
        print(f"You found the number correctly after {counter} attempts")

def main():
    name = input("Please Enter Your name : ").strip().upper()
    print(f"Welcome {name} !!!")
    print("Game Instructions : \n => Try to guess the right number ")
    print("======================================================================================")
    game()

main()