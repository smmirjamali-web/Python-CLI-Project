import random

secret = random.randint(1,100)

print("Guess the number (between 1 and 100)")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a number")
        continue

    guess = int(guess)
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100")
        continue

    if guess < secret:
        print("Your guess is too low")
    elif guess > secret:
        print("Your guess is too high")
    else:
        print("Correct!!! You guessed the number!")
        break