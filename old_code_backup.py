
# alternative to __str__ for the Chessboard class (try to fix the str expected error, but Rook found)
"""def print_board(self):
    final = ''
    for i in range(17):
        if i == 16:
            print("\t" + "\t".join([str(i + 1) for i in range(8)]))
        elif i % 2 == 1:
            print("\t" + '-' * 33 + '\n')
        elif i % 2 == 0:
            print(chr(i // 2 + 97) + "   | " + " | ".join(self.board[i // 2]) + " | \n")"""

# unknown code
"""class Nknight(Chesspiece):
    def move_list(self, board):
        self.can_go_to = {(self.position[0] + j, self.position[1] + i) for i in range(-1, 2, 1) for j in range(-1, 2, 1) if
             (self.position[0], self.position[1]) != (
             self.position[0] + j, self.position[1] + i) and board.available_case(
                 (self.position[0] + j, self.position[1] + i), self.color)}
        # x = {(self.position[0], self.position[1]) for i in range(8) if board.available_case((self.position[0] + 1, self.position[1] - 1 + i), self.color)}
        print(self.can_go_to)

        return self.can_go_to"""

# old unfinished version rook calculaion
"""def move_calculation(self, board):
    a, s, d, w = True
    x = 1
    self.can_go_to = {}
    while w or s or a or w or d:
        if w and board.available_case(self.position[0], self.position[1] + x):
            # if

            pass

        yield (0, -x)
        yield (x, 0)
        yield (-x, 0)
        x += 1
"""