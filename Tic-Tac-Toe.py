#!/usr/bin/python

import sys
from texttable import Texttable
import time


def display_board(board):
    table = Texttable()  # Create a table
    table.add_rows([[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]])
    table.set_chars(['-', '|', '+', '-'])  # to draw lines between rows & columns [horizontal, vertical, corner, header]
    print(table.draw())  # table is returned as a whole string


def position_check_add(board, person_playing):
    global player
    try:
        pos_choice = int(input("Which position (1-9) do you want to play? : "))
        if board[pos_choice - 1] in range(1, 10):
            if pos_choice in range(1, 10):
                board[pos_choice - 1] = person_playing
                player += 1
                display_board(board)
            else:
                print("Enter a valid position from 1-9")
                position_check_add(board, person_playing)
        else:
            print("That position is already played!! Please select another!!")
            position_check_add(board, person_playing)
    except KeyboardInterrupt and EOFError:
        print("\n\t\t\tPlayer Interrupted!!\n\t\t\t Exiting!!")
        sys.exit()  # Exits from the program
    except:
        print("Invalid Input!! Please enter an integer from 1-9!!")
        position_check_add(board, person_playing)


def replay():
    global Game_On, myBoard, player
    play_again = input("Do you want to play again?? (Yes/No)")
    if play_again == "Yes" or play_again == "Y":
        myBoard, Game_On, player = initial()
    elif play_again == "No" or play_again == "N":
        Game_On = False
        print("\n\t\t\t Game Over!!!")
        time.sleep(10)
    else:
        print("Invalid Option selected!! Please enter Yes or No ")


def initial():
    print("             Welcome to Tic-Tac-Toe Game!!!                ")
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_on = True
    player_init = 1
    display_board(board)
    # player1 = input("Do you want to be Player 'X' or Player 'O':  ")
    print("\n\t\t\tThe one who plays first marks 'X' and the other 'O' !!\n\t\t\tPlayer 1 --> X\n\t\t\tPlayer 2 --> O")
    return board, game_on, player_init


if __name__ == '__main__':
    myBoard, Game_On, player = initial()
    while Game_On:
        if player % 2 != 0:
            person = 'X'
        else:
            person = 'O'

        position_check_add(myBoard, person)

        if (myBoard[0] == myBoard[1] == myBoard[2]) or (myBoard[0] == myBoard[3] == myBoard[6]) or (myBoard[0] == myBoard[4] == myBoard[8]):
            print(f"\t\t\t{myBoard[0]} Won!!")
            winner = myBoard[0]
            replay()
        elif (myBoard[3] == myBoard[4] == myBoard[5]) or (myBoard[1] == myBoard[4] == myBoard[7]):
            print(f"\t\t\t{myBoard[4]} Won!!")
            replay()
        elif (myBoard[6] == myBoard[7] == myBoard[8]) or (myBoard[2] == myBoard[5] == myBoard[8]):
            print(f"\t\t\t{myBoard[8]} Won!!")
            replay()
        elif myBoard[2] == myBoard[4] == myBoard[6]:
            print(f"\t\t\t{myBoard[2]} Won!!")
            replay()
        elif (''.join(str(i) for i in myBoard)).isalpha():  # Checks if the board is fully played
            print("\t\t\t\tGame Draw!!!")
            replay()
        else:
            continue
