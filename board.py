from btree import LinkedBinaryTree


class IndexError(Exception):

    def __str__(self):
        return 'Your move is not valid, pleasy do a right one.'


class Board:

    def __init__(self):
        self.computer_player = '0'
        self.user_player = 'х'
        self._height, self._width = 3, 3
        self.board = [['' for i in range(self._width)] for j in range(self._height)]
        self.last_move = None

    def get_status(self):
        players = ['x', '0']
        for player in players:
            for column in range(3):
                if self.board[0][column] == self.board[1][column] == self.board[2][column] == player:
                    return player
            for row in range(3):
                if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                    return player
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
                return player
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
                return player
        for position in self.board:
            if '' in position:
                return "continue"
        else:
            return "draw"

    def check_valid(self, position):
        try:
            if self.board[position[0]][position[1]] == '':
                return True
        except IndexError:
            return False

    def __str__(self):
        result = ""
        for row in self.board:
            result += str(row) + "\n"
        return result

    def make_move(self, position, turn):
        if not self.check_valid(position):
            raise IndexError('Please write correct place on the board!')
        self.last_move = (position, turn)
        self._add(position, turn)
        return self

    def _board_el_in_row(self):
        result = []
        for row in self.board:
            for element in row:
                result.append(element)
        return result

    def _fill_board(self, list_of_borad_elments):
        counter = 0
        for row in range(self._height):
            for column in range(self._width):
                self.board[row][column] = list_of_borad_elments[counter]
                counter += 1

    def _add(self, position, sign):
        self.board[position[0]][position[1]] = sign

    def copy_actual_board(self):
        board = self._board_el_in_row()
        new_board = Board()
        new_board._fill_board(board)
        return new_board

    def possible_movemnts(self):
        result = []
        for row in range(self._width):
            for column in range(self._height):
                if len(result) == 2:
                    return result
                if self.board[row][column] == '':
                    result.append(tuple((row, column)))
        return result

    def make_computer_move(self):
        copied_actual_board = self.copy_actual_board()
        tree = LinkedBinaryTree(copied_actual_board)

        def recursive(tree, board, sign_):
            left_branch = board.copy_actual_board()
            right_branch = board.copy_actual_board()
            possible_moves = board.possible_movemnts()
            if len(possible_moves) == 0:
                return
            if len(possible_moves) == 1:
                possible_moves.append(possible_moves[0])
            sign = '0' if sign_ == 'x' else 'x'
            if self.get_status() == 'continue':
                left_branch.make_move(possible_moves[0], sign_)
                tree_left = tree.insert_left(left_branch)
                recursive(tree_left, left_branch, sign)
            if left_branch.get_status() == 'continue':
                right_branch.make_move(possible_moves[1], sign_)
                tree_right = tree.insert_right(right_branch)
                if right_branch.get_status() == 'continue':
                    recursive(tree_right, right_branch, sign)

        recursive(tree, copied_actual_board, '0')

        def get_points(tree):
            points = 0

            def recursive(tree, points):
                try:
                    board = tree.key
                except AttributeError:
                    return points

                if board.get_status() == "continue":
                    points += recursive(tree.left_child, points)
                    points += recursive(tree.right_child, points)
                    return points

                elif board.get_status() == self.computer_player:
                    points += 1
                    return points
                elif board.get_status() == self.user_player:
                    points -= 1
                    return points

                else:
                    return points

            return recursive(tree, points)
        # try:
        #     left_tree_branch = tree.left_child.key
        # except AttributeError:
        left_tree_branch = tree.left_child.key

        # left_tree_branch = tree
        # print(left_tree_branch)
        right_tree_branch = tree.right_child.key
        left_points = get_points(tree.left_child)
        right_points = get_points(tree.right_child)
        # print('----')
        # print(left_points)
        # print(right_points)
        # print('----')
        if left_points >= right_points:
            self.make_move(left_tree_branch.last_move[0], left_tree_branch.last_move[1])
        else:
            self.make_move(right_tree_branch.last_move[0], right_tree_branch.last_move[1])
