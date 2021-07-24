# 1) draw the grid use print statements                -done
# 2) let the user check if they want to be x or o      -done
# 3) write a function that takes in a position and returns a position  -done
# 4) inputs x or y in the right box and displays the new box - done
# 5) do win check tell the player they won              -done check if all x or o
# 6) create a function to choose whether player 1 or 2 should go first - done
# 7) check whether the space on the box is empty      -done
# 8) check if the board is already full - check if  all 9 boxes are full - done
# 9) ask if they want to replay again
import random

def player_choice(board):

    # position = int(input("\nWhat position would you like to enter? [1-9]\n"))
    # while (position < 1 or position > 9) or not (space_check(board, position)): #condition is automatically set to True
    #     position = int(input("\nYour position is not valid. Please try again: [1-9]\n"))
    while True:
        #with error handling used in case we type letters instead of numbers (int)
        try:
            position = int(input("\nWhat position would you like to enter? [1-9]\n"))
        except:
            print("This is not a number please try again.")
        else:
            if position >= 1 and position <= 9:
                break

    return position

def space_check(board, position):
    return board[position] != "X" and board[position] != "O"


def win_check(board, marker):

    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[2] == marker and board[5] == marker and board[8] == marker) or
    (board[3] == marker and board[6] == marker and board[9] == marker) or
    (board[1] == marker and board[5] == marker and board[9] == marker) or
    (board[3] == marker and board[5] == marker and board[7] == marker))

def player_input():
    player_1_marker = ""
    while (player_1_marker != "X" and player_1_marker != "O"):
        player_1_marker = input("\nPlayer 1, do you want to be noughts or crosses? [O,X]\n").upper()

    if player_1_marker == "X":
        player_2_marker = "O"
    else:
        player_2_marker = "X"

    return player_1_marker, player_2_marker

#player_1_marker, player_2_marker = player_input() //the function is called and the values are returned back to it and assigned tp the variables on the lhs


def display_board(board):

    print("   |   |   ")
    print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " " )
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " ")
    print("   |   |   ")

#display_board(board) #board = ["#","X","O","X","O","X","O","X","O","X"]

def place_marker(board, position, marker):
    board[position] = marker

def choose_first():
    output = random.randint(0,1)
    player_list = ["player_1", "player_2"]
    return player_list[output] #everything that has a return needs to be assigned

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def replay():
   repeat = input("\nWould you like to play again?[Y/N]\n")
   return repeat.upper() == "Y"

#run the game
while True:
    play_game = input('\nAre you ready to play? [y/n]\n')
    board = [" "] * 10
    display_board(board)

    if play_game.lower() == 'y':
        game_on = True
        player1_marker, player2_marker = player_input()  # move above
        turn = choose_first()
    else:
        print("\nThanks for playing, see you next time.")
        game_on = False
        break

    while game_on:
        if turn == "player_1":
            print("\nIt is player one's turn:")
            display_board(board)
            position = player_choice(board)
            place_marker(board, position, player1_marker)
            if win_check(board,player1_marker):
                display_board(board)
                print("\nCongratulations you have won the game!")
                break
            else:
                if full_board_check(board):
                    display_board(board)
                    print("\nIt is a draw.")
                    break
            turn = "player_2"

        else:
            print("\nIt is player two's turn:")
            display_board(board)
            position = player_choice(board)
            place_marker(board, position, player2_marker)
            if win_check(board, player2_marker):
                display_board(board)
                print("\nCongratulations you have won the game!")
                break
            else:
                if full_board_check(board):
                    display_board(board)
                    print("\nIt is a draw.")
                    break
            turn = "player_1"

    if not replay(): # not replay() - evaluates to the condition True so the code below runs
        print("\nThanks for playing, see you again.\n")
        break


    print("\nIt is player one's turn:")


