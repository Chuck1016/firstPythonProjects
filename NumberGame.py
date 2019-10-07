import random
print("Hello, what's your name?")
name = input()
print("Well " + name + ", I'm thinking of a number between 1 and 10")
print("Can you guess what number I'm thinking of?")
secretNumber = random.randint(1,10)
for guesses in range(1,6):
    guess = int(input())
    if guess < secretNumber:
        print('Your guess it too low. Try a higher number')
    elif guess > secretNumber:
        print('Your guess is too high. Try a lower number')
    else:
        break

if guess == secretNumber:
    print("Good job " + name + "! You guessed my number in " + str(guesses) + " tries.")
else:
    print("Nope, The number I was thinking of was " + str(secretNumber ))
input()	
	
##  from Automate the Boring Stuff With Pythonby Al Sweiger	
