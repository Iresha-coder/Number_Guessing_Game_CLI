from random import randint

global difficulty_level

def select_difficulty():
    global difficulty_level
    difficulty = input("Select you difficulty\n(type it in numbers)\n1.Easy\n2.Medium\n3.Hard\n: ")
    if difficulty == "1":
        difficulty_level = "1"
    elif difficulty == "2":
        difficulty_level = "2"
    elif difficulty == "3":
        difficulty_level = "3"
    else:
        print("Try again and type a valid number")
        select_difficulty()

print("Welcome to this Number Guessing Game!")

score = 0
guesses = 0

select_difficulty()

while True:
    global difficulty_level

    if difficulty_level == "1":
        random_number = randint(1, 10)
        while True:
            answer = input("Guess the number: ")
            if answer.lower() == "q":
                quit()
            if int(answer) == random_number:
                print("You're correct")
                break
            elif int(answer) != random_number:
                print("You're wrong! Try again")
                continue
    elif difficulty_level == "2":
        random_number = randint(1, 20)
        while True:
            answer = input("Guess the number: ")
            if answer.lower() == "q":
                quit()
            if int(answer) == random_number:
                print("You're correct")
                break
            elif int(answer) != random_number:
                print("You're wrong! Try again")
                continue
    elif difficulty_level == "3":
        random_number = randint(1, 40)
        while True:
            answer = input("Guess the number: ")
            if answer.lower() == "q":
                quit()
            if int(answer) == random_number:
                print("You're correct")
                break
            elif int(answer) != random_number:
                print("You're wrong! Try again")
                continue
