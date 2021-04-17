import random

words_list = ['apple', 'orange', 'banana', 'grape', 'mango']
print('Welcome to hangman\n')

def hangman_setup(number_of_lives):
    print(f"The number of lives you have are {number_of_lives}.\n")
    ans_word = words_list[random.randint(0, len(words_list) - 1)]
    prog_word = '_' * len(ans_word)
    return ans_word, prog_word

def replay():
    play_again = input("\nDo you want to play again? [y/n]\n")
    return play_again.lower() == "y"

while True:
    number_of_lives = 3
    ans_word, prog_word = hangman_setup(number_of_lives)
    play_game = input("Are you ready to play? [y/n]\n")

    if play_game.lower() == "y":
        game_on = True
    else:
        print("\nThanks for playing, see you next time.")
        game_on = False
        break

    print(f"\nHint the number of words the ans has is {len(ans_word)}.")
    print(prog_word)

    while game_on:

        if prog_word == ans_word:
            print("\nCongratulations for completing the game!\n")
            break
        elif number_of_lives == 0:
            print("\nSorry you have lost the game.\n")
            break
        else:
            guess_letter = input("\nTake a guess\n")
            prog_word_list = list(prog_word)
            if guess_letter in ans_word:
                for i in range(len(ans_word)):
                    if guess_letter == ans_word[i]:
                        prog_word_list[i] = guess_letter
                prog_word = ''.join(prog_word_list)
                print(prog_word)
            else:
                number_of_lives -= 1
                print("\nWrong guess, try again.\n")
                print(f"\nYou have {number_of_lives} lives left.\n")
                print(prog_word)

    if not replay():
        print("\nThanks for playing, see you again.\n")
        break