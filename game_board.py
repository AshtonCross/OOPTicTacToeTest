class GameBoard:

    # define the actual playspace.

    def __init__(self, board_format):
        self.board_format = board_format

        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

    def is_valid_move(self, pillar, row):
        # this function validates the move *AND offsets the input to match the array*

        try:
            row = int(row)
            pillar = int(pillar)

            row -= 1
            pillar = abs(3 - pillar)   

            if (self.board[pillar][row] == '-'):
                return True, pillar, row    
                
        except (TypeError, ValueError, IndexError):
            pass

        return False, pillar, row


    def place_move(self, character_input, pillar, row):
        # place move
        self.board[pillar][row] = character_input


    def str_boxy(self):
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


    def str_classic(self):
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


    def str_normal(self):
        formatted_board = ''

        for row in self.board:
            for space in row:
                formatted_board += space + ' '

            formatted_board += '\n'

        return formatted_board


    def str_format(self):
        if self.board_format == 'normal':
            return self.str_normal()
        elif self.board_format == 'boxy':
            return self.str_boxy()
        elif self.board_format == 'classic':
            return self.str_classic()
        else:
            raise Exception('Unknown format type \'' + self.board_format + '\'.')


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
        left_to_right = self.board[0][0] + self.board[1][1] + self.board[2][2]

        if left_to_right == 'xxx':
            return 'x'
        elif left_to_right == 'ooo':
            return 'o'

        # right to left diagonal
        right_to_left = self.board[2][0] + self.board[1][1] + self.board[0][2]

        if right_to_left == 'xxx':
            return 'x'
        elif right_to_left == 'ooo':
            return 'o'

        return None
        
    def isFull(self):
        for x in self.board:
            for y in x:
                if y == '-':
                    return False

        return True
