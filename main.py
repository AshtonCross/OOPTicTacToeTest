# here's a fun little project i threw together to learn object-oriented programming
# Ashton Cross 2-10-2022

import sys

from game_board import GameBoard

def take_move_input(in_str):
    while True:
        move = input(in_str)
        move = move.strip().upper()

        if move == 'EXIT':
            sys.exit()
        if move == 'PRINT':
            print(board.str_format())
            continue

        return move


def menu():
    print("Tic Tac Toe")
    print("Select Game Board Type:\n")
    menu_input = input("1. Normal\n2. Box\n3. Napkin\n4. exit\n\n>")

    # lower case so that we don't have to worry about caps when comparing
    menu_input = menu_input.lower()

    while True:
        if menu_input == "normal" or menu_input == '1':
            game('normal')
            menu()
        elif menu_input == "box" or menu_input == '2':
            game('boxy')
            menu()
        elif menu_input == 'napkin' or menu_input == '3':
            game('classic')
            menu()
        elif menu_input == "exit" or menu_input == '4':
            sys.exit()
        else:
            # no valid input detected; trying again
            menu()

def game(board_format):
    board = GameBoard(board_format)
    round_number = 1

    while True:

        # print game board
        print("\n\nRound", round_number)
        print(board.str_format())

        # decide who's turn it is
        if round_number % 2 == 0:
            player = 'o'
            print("\nplayer 2 (o)")
        else:
            player = 'x'
            print("\nplayer 1 (x)")

        # place move
        while True:

            row = take_move_input('\nEnter Desired Pillar: ')
            pillar = take_move_input('Enter Desired Row: ')

            valid_move, pillar, row = board.is_valid_move(pillar, row)

            if not valid_move:
                print('invalid move')
                continue

            # input has been offset by the valid move function
            board.place_move(player, pillar, row)
            print(board.str_format())
            break


        # check for winner
        winner_decision = board.win_check()

        if winner_decision == 'x':
            print("Player 1 (x) wins!")
            input()
            return

        elif winner_decision == 'o':
            print("Player 2 (o) wins!")
            input()
            return

        # if there's no winner, check if the board is full and if
        # there's a stalemate.

        if board.isFull():
            print(board.str_format())
            print("\nStalemate!")
            input()
            return

        # prep for next round
        round_number += 1


if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        pass
