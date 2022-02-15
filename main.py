import sys

from game_board import GameBoard


def main():

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
        board = GameBoard()
        game_is_over = False
        round_number = 1

        while not game_is_over:

            # print game board
            print("\n\nRound", round_number)
            print(board.str_format(board_format))

            # decide who's turn it is
            if round_number % 2 == 0:
                player = 'o'
                print("\nplayer 2 (o)")
            else:
                player = 'x'
                print("\nplayer 1 (x)")

            # place move
            while True:

                row = input('\nEnter Desired Pillar: ')
                try:
                    row = int(row)
                except:
                    if row == 'PRINT':
                        print(board.str_format(board_format))
                        continue
                    elif row == 'EXIT':
                        sys.exit()
                    else:
                        print('invalid move')
                        continue

                pillar = input('Enter Desired Row: ')
                try:
                    pillar = int(pillar)
                except:
                    if pillar == 'PRINT':
                        print(board.str_format(board_format))
                        continue
                    elif pillar == 'EXIT':
                        sys.exit()
                    else:
                        print('invalid move')
                        continue

                # format the input so it makes more sense
                row -= 1

                if pillar == 1:
                    pillar = 2
                elif pillar == 2:
                    pillar = 1
                elif pillar == 3:
                    pillar = 0

                # place the move if it is a valid move
                if board.is_valid_move(pillar, row):
                    board.place_move(player, pillar, row)
                    break
                else:
                    continue

            # check for winner
            winner_decision = board.win_check()

            if winner_decision == 'x':
                print(board.str_format(board_format))
                print("Player 1 (x) wins!")
                input()
                game_is_over = True
            elif winner_decision == 'o':
                print(board.str_format(board_format))
                print("Player 2 (o) wins!")
                input()
                game_is_over = True

            # prep for next round
            round_number += 1

    menu()


if __name__ == '__main__':
    main()
