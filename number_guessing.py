# computer randomly chooses a number between 1 to 100
# random.randint(0,100)
# store the number in a variable
# print the computer has randomly generated a number

# person guesses the number:
# first guess: input number

# if the number is within range 10 of the random number -> "warm"
# if (random number - input number < 10 and random number - input number = 10) or (input number - random number < 10 and input number - random number = 10)
#print warm

# if the number is greater than the range of 10 of the random number ->
# if the guess is out of range tell them it's out of range

# if the range gets smaller -> "warmer"
# if the range is greater than before -> "colder"


import random
 # if the play_again function makes things complicated then just take the code and put it inside the while loop

print("Welcome to number guessing!\n")
play = input("Would you like to play a game? [Y/N] \n")

if play == "Y".lower():
    game_on = True
else:
    game_on = False
    print("Okay, see you later!")

while game_on:

    computer_choice = random.randint(0, 100)
    print(computer_choice)

    print("The computer has chosen a random number.\n")

    human_choice = int(input("Please input your number of choice: \n"))

    if computer_choice == human_choice:
        print("Congratulations you have guessed correctly!\n")
        repeat = input("Would you like to play again? [Y/N]\n")
        if repeat == "Y".lower():
            game_on = True  #no break will just jump to the top of the while loop where the game_on = True
        else:
            game_on = False
            print("Okay no worries. See you next time!\n")
            break
    elif abs(computer_choice - human_choice) < 11:
        print("You are warm\n")
    else:
        print("You are cold\n")


    while human_choice != computer_choice:
        human_choice_2 = int(input("Have another go:\n"))

        if computer_choice == human_choice_2:
            print("Congratulations you have guessed correctly!\n")
            repeat = input("Would you like to play again? [Y/N]\n")
            if repeat == "Y".lower():
                game_on = True
                break
            else:
                game_on = False
                print("Okay no worries. See you next time!\n")
                break
        elif abs(computer_choice - human_choice) > abs(computer_choice - human_choice_2):
            print("You are getting warmer, try again.\n")
        elif abs(computer_choice - human_choice) < abs(computer_choice - human_choice_2):
            print("You are getting colder, have another go.\n")

        human_choice = human_choice_2

