import random

secret_number = random.randint(1, 20)
for attempt in range(5):
    guess = input(f"Attempt {attempt + 1}: ")
    if not guess.isdigit(): print("Invalid input!"); continue
    guess = int(guess)
    if guess == secret_number: print("You guessed it!"); break
    elif guess < secret_number: print("Too low!")
    else: print("Too high!")
else: print("Out of attempts! The number was", secret_number)
