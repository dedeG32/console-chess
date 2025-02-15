from plateau import Chessboard
chessboard = Chessboard()
chessboard.init_board()

def menu():
    print("select your game mode:")
    print("1. guide")
    print("2. Player Vs Computer (I need one more year to make that -sorry)")
    print("3. Player Vs Player")
    chose = get_int(1,3)

    match chose:
        case 1:
            guide()
        case 2:
            print("Told you! Nothing here.")
            menu()
        case 3:
            start_1v1_chess()

def start_1v1_chess():


    game = True
    p=0
    while game:
        p+= 1
        pos = player_turn('black' if p//2 ==0 else "white")

def player_turn(color):
    while True:
        get_case_corectformat(color)

def get_case_corectformat(color):

    input = None
    while not chessboard.valid_input(input):
        input = input(color + " turn: ", end="").lower()

def guide():
    print('\nA simple chess game requiring 2 players.\n\nPieces are formatted in a way the color is the first letter and the piece is the second. For exemple: black king = "bK".\nThe second letter represent the piece. Below are all the pieces:\nKing = K\nQueen = Q\nKnight = N\nBishop = B\nRook = R\n\nTo move a piece you need to first indicate it position (letter followed by a number. Exemple: e5), followed by a space, and then the case you want it to go.\nFor exemple: "e5 f4" (note that the format[xx xx] must be followed).\nYou can leave the game at any time inputting "0".\n\nEnjoy your game!')
    menu()

def get_int(min, max) -> int:
    while True:
       try:
            chose = int(input("Enter: "))
            if min <= chose <= max:
                return chose
            else:
                print(f"please input a number between {min} and {max}")
       except :
            print("Please enter a valid integer")


def setup_game():
    pass

if __name__ == "__main__":
    menu()