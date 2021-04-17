import random

# input q - Do you want to play? [y/n]
# if no - thanks see you again
# if yes - input q - Choose between rock, paper, scissors - input r,p,s
# choose one - store in variable
# computer randomly generates r, p, s

# user_games_won = 0
# comp_games_won = 0

# if user == r and computer == s or user == p and computer == r or user == s and computer == p - user wins - user+=1
# if user == s and computer == r or user == r and computer == p or user == p and computer == s - user looses - comp+=1
# if user == r and computer == r or user == s and computer == s or user == p and computer == p - draw

# input q - Do you want to play again? [y/n]
# if no - thanks see you again - break while loop
# if yes - continue the while loop
# could do up to 3 games

rps = ['rock', 'paper', 'scissors']

print('Welcome to rock, paper, scissors\n')

def replay():
    play_again = input('\nDo you want to play again? [y/n]\n')
    return play_again.lower() == 'y'

while True:
    game_score = 0
    user_score = 0
    comp_score = 0
    play_game = input('\nAre you ready to play? [y/n]\n')

    if play_game.lower() == 'y':
        game_on = True
        print('You have three rounds for each game:')
    else:
        game_on = False
        break

    while game_on:

        if game_score == 3:
            if user_score > comp_score:
                print(f'The user score is {user_score} and the computer score is {comp_score}. Congratulations you have won!\n')
            elif comp_score > user_score:
                print(f'The computer score is {comp_score} and the user score is {user_score}. Unfortunately you have lost\n')
            else:
                print(f'The computer score is {comp_score} and the user score is {user_score}. You have drawn.\n')
            game_on = False

        else:
            comp_input = rps[random.randint(0, len(rps)-1)]
            user_input = input('\nChoose either rock(R), paper(P) or scissors(S): \n').upper()
            game_score += 1

            if user_input == 'R':
                print(f'For round {game_score}: You have chosen rock and the computer has chosen {comp_input}.\n')
            elif user_input == 'P':
                print(f'For round {game_score}: You have chosen paper and the computer has chosen {comp_input}.\n')
            else:
                print(f'For round {game_score}: You have chosen scissors and the computer has chosen {comp_input}.\n')

            if (user_input == 'R' and comp_input == rps[2]) or (user_input == 'S' and comp_input == rps[1]) or (user_input == 'P' and comp_input == rps[0]):
                user_score += 1
                print('\nYou won\n')
            elif (user_input == 'R' and comp_input == rps[0]) or (user_input == 'P' and comp_input == rps[1]) or (user_input == 'S' and comp_input == rps[2]):
                print('\nIt\'s a draw\n')
            else:
                comp_score += 1
                print('\nYou lost\n')

    if not replay():
        print("\nThanks for playing, see you again.\n")
        break