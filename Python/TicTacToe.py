#Creating a list of list, so that we get a matrix style

import enum

game = [[0,0,0],[0,0,0],[0,0,0]]
def game_board():
    print("   0, 1, 2")
    for index, row in enumerate(game):
        print(index, row)
game_board()



