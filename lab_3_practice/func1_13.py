import random
name = input("Hello! What is your name? ")
number = random.randint(1, 20)
print("Well, " + name + ", I am thinking of a number between 1 and 20."'\n')
guessestaken = 0
while guessestaken<100:
    guess = input("Take a guess. ")
    guess = int(guess)
    guessestaken = guessestaken + 1
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Good job, " + name + "! You guessed my number in " + str(guessestaken) + " guesses!")
        break
