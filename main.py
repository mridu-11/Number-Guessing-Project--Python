import random
import art

print(art.logo2)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level= input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number= random.randint(1,100)

def attempts(number):
    print(f"You have {number} attempts remaining to guess the number.")

if difficulty_level == "easy":
    number_of_attempts = 10
else:
    number_of_attempts = 5

game_on=True
while game_on:
    attempts(number_of_attempts)
    player_guess = int(input("Make a Guess: "))
    if player_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_on = False
    else:
        if player_guess > random_number:
            print("Too High")
        else:
            print("Too Low")
        number_of_attempts -= 1
        if number_of_attempts!=0:
            print("Guess again.")
        else:
            print("You've run out of guesses. Refresh the page to run again.")
            game_on= False
