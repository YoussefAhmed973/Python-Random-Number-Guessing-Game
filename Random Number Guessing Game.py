#Import module
import random
random.random()
numb_generator = random.randint(1, 10)

#User Input
user_input = int(input("Choose a random number between 1 and 10: "))

#Compare Input to Random Number
if user_input == numb_generator:
    print("You have guessed correctly, the answer was ", user_input)

elif user_input > 10:
    print("I said a number between 1 and 10 >:(")

else:
    print("Incorrct guess, better luck next time. The correct number was " + str(numb_generator))


