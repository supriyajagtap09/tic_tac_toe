import random

# first pick a random integer from 1 to 100
num = random.randint(1,100)
print(num)

# introducing the rules of the game
print("Welcome To Guess Me...!")
print("I'm thinking of a number between 1 & 100")
print("If your guess is more than 10 away from my numbers, I will tell you are COLD")
print("If your guess is within 10 of my number, I will tell you are WARM")
print("If your guess is farther than your most recent guess, I will say you are getting COLDER")
print("If your guess is closer than your most recent guess, I will say you are getting WARMER")
print("Let's Play")

# create list to store guesses
guesses = [0]

# Players guess

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    break


while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    # if guess is incorrect, add guess to the list
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num - guesses[-1]) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')


