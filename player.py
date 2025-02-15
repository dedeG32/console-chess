class Player(object):
    def __init__(self):
        self.color = "white"

    def get_input(self):
        while True:
            input = input(self.color +" turn: ", end="")
            if len(input) != 5 and input[2]!=" ":
                print('Incorect format! try a format like "x9 x9"')

            if input[:1]==input[3:]:
                print("")