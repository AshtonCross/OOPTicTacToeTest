class GameBoard:

    # define the actual playspace.

    def __init__(self):
        self._last_move = list()  # will contain cooridinates for undo function (might not even get used)

        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

    def is_valid_move(self, pillar, row):
        if not self.board[pillar][row] == '-':
            return False
        else:
            return True

    # undo move if necessary. Not tested yet. Don't use.
    def undo_move(self):
        if self._last_move == list():
            pass
        else:
            pillar = self._last_move[0]
            row = self._last_move[1]
            self.place_move('-', pillar, row)

    def place_move(self, character_input, pillar, row):
        # place move
        self.board[pillar][row] = character_input
        self._last_move = [pillar, row]

    def str_format(self, style='normal'):

        # default and somewhat plain format style
        if style == 'normal':
            formatted_board = ''

            for row in self.board:
                for space in row:
                    formatted_board += space + ' '

                formatted_board += '\n'

            return formatted_board

        # boxy style
        elif style == 'boxy':
            formatted_board = ''

            # row_position = 0
            formatted_board += '+---+---+---+\n'

            for row in self.board:

                space_position = 0
                for space in row:

                    if space_position == 0:
                        formatted_board += '| ' + space + ' | '
                    else:
                        formatted_board += space + ' | '

                    space_position += 1

                # row_position += 1
                formatted_board += '\n+---+---+---+\n'

            return formatted_board

        # classic style
        elif style == 'classic':
            formatted_board = ''

            row_position = 0

            for row in self.board:

                if 0 < row_position < 3:
                    formatted_board += '\n---+---+---\n'

                space_position = 0
                for space in row:

                    if space_position == 0:
                        formatted_board += ' ' + space + ' | '
                    elif space_position == 2:
                        formatted_board += space
                    else:
                        formatted_board += space + ' | '

                    space_position += 1

                row_position += 1

            return formatted_board

        # technical, for running tests on the board
        if style == 'technical':
            formatted_board = ''

            for row in self.board:
                for space in row:
                    formatted_board += space

            return formatted_board

        # what even are you asking me to do???
        else:
            raise Exception('Unknown format type \'' + style + '\'.')

    def win_check(self):
        # return 'x' or 'o' or None if no winner

        # row checks !!!
        for row in self.board:
            this_row = ''

            for space in row:
                this_row += space

            if this_row == 'xxx':
                return 'x'
            elif this_row == 'ooo':
                return 'o'

        # pillar check
        for pillar in range(3):
            this_pillar = ''

            for row in self.board:
                this_pillar += row[pillar]

            if this_pillar == 'xxx':
                return 'x'
            elif this_pillar == 'ooo':
                return 'o'

        # left to right diagonal
        left_to_right = self.str_format("technical")[0] + self.str_format("technical")[4] + self.str_format("technical")[8]

        if left_to_right == 'xxx':
            return 'x'
        elif left_to_right == 'ooo':
            return 'o'

        # right to left diagonal
        right_to_left = self.str_format("technical")[2] + self.str_format("technical")[4] + self.str_format("technical")[6]

        if right_to_left == 'xxx':
            return 'x'
        elif right_to_left == 'ooo':
            return 'o'

        return None

