import sys

num = int(input("Enter a number for the other player to guess: "))
guess = int(input("Guess the number: \n"))
while (guess != num):
    hint = input("Wrong. Want a hint? ")
    if (hint == "yes" or hint == "y"):
        if  (guess > num): print("OK, so it is less than " + str(guess))
        else: print("OK, so it is bigger than " + str(guess))
    secondChance = input("Care to try again? ")
    if (secondChance == "y" or secondChance == "yes"):
        guess = int(input('Guess the number: \n'))
    else:
        print("Awww. You were so close. The correct answer was " + str(num))
        exit()
    guess = int(guess)
print("\nWell done! The number was " + str(num))
