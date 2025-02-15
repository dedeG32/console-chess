import chess_pieces
import plateau

def main_chess():
    chessboard = plateau.Chessboard()

    #chessboard.init_board()

    # chessboard.put_piece( chess_pieces.Bishop("white", (4, 3)))
    # chessboard.put_piece(chess_pieces.Pawn("black", (4, 4)))
    #
    # for _ in range(10):
    #     chessboard.print_board()
    #     chessboard.move_piece(input())
    chessboard.game_loop()


if __name__ == '__main__':
    main_chess()