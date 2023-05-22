import pygame as pg

_ = False
mini_map = [
    [3,2,1,1,2,1,1,3,3,2,2,3,2,3,2,3,1,2,1,3,2,2],
    [3,_,_,_,_,_,_,2,_,_,_,_,_,_,2,_,_,_,_,_,_,2],
    [3,_,_,_,_,_,_,2,_,_,_,_,_,_,2,_,_,_,_,_,_,2],
    [2,_,_,_,_,_,_,3,_,_,_,_,_,_,3,_,_,_,_,_,_,2],
    [2,_,_,_,_,_,_,2,_,_,_,_,_,_,3,_,_,_,_,_,_,2],
    [2,_,_,_,_,_,_,2,_,_,_,_,_,_,2,_,_,_,_,_,_,2],
    [3,_,_,_,_,_,_,3,_,_,_,_,_,_,2,_,_,_,_,_,_,2],
    [3,2,2,3,2,2,3,2,_,_,_,_,_,_,2,3,2,2,3,2,2,2],
    [2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2],
    [3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,3],
    [3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2],
    [2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,3],
    [1,2,3,2,2,3,4,_,_,_,_,_,_,4,2,3,2,3,3,2,2,2],
    [1,_,_,_,_,4,4,4,_,_,_,_,4,4,4,6,5,6,4,3,2,2],
    [2,_,_,_,_,4,4,4,4,_,_,5,4,4,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,4,_,_,4,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,4,_,_,4,_,_,_,_,_,_,_,4,_,1],
    [2,_,_,_,_,4,_,_,4,_,_,_,_,_,_,_,_,_,_,5,_,1],
    [1,_,_,_,_,4,_,_,4,_,_,_,_,_,_,_,_,_,_,4,_,1],
    [3,_,_,_,_,4,_,_,4,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,4,4,4,5,5,5,4,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,4,4,4,4,4,_,4,_,2],
    [3,_,_,_,_,5,_,_,_,_,_,_,_,_,_,_,_,4,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,5,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,5,_,4,_,2],
    [3,_,_,_,_,5,_,_,_,4,_,_,_,4,_,_,_,4,_,4,_,2],
    [3,_,_,_,_,5,_,4,5,4,5,4,_,6,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,4,_,_,_,4,_,_,_,_,_,6,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,4,4,5,5,4,4,_,2],
    [3,_,_,_,_,6,_,_,_,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,4,_,_,_,_,_,_,_,_,_,_,5,_,2],
    [3,_,_,_,_,5,_,_,4,5,4,5,4,5,5,4,_,_,_,5,_,2],
    [3,_,_,_,_,4,4,5,4,_,_,_,_,_,_,4,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,6,_,_,_,5,_,2],
    [3,_,_,_,_,5,_,_,_,_,_,_,_,_,_,4,_,_,_,5,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,5,_,2],
    [3,_,_,_,_,6,_,_,4,5,4,4,4,5,4,4,5,4,5,4,_,2],
    [3,_,_,_,_,5,_,_,4,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,4,_,_,_,4,_,_,_,4,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,5,_,_,_,4,4,_,4,4,_,_,4,_,2],
    [3,_,_,_,_,6,_,_,4,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,5,_,_,5,_,_,4,5,5,4,4,4,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,5,_,_,_,_,5,_,_,6,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,4,_,_,_,_,5,_,_,4,_,2],
    [3,_,_,_,_,4,4,5,4,5,4,4,_,_,_,_,4,_,_,5,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,4,4,5,6,4,5,4,5,5,7,_,2],
    [3,_,_,_,_,4,_,5,4,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [3,_,_,_,_,4,_,4,5,_,_,_,5,4,_,_,_,4,_,9,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [3,_,_,_,_,7,7,7,7,7,8,7,7,7,9,7,_,_,7,7,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,_,_,_,_,4,_,_,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,4,_,_,_,_,_,_,5,4,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,4,5,4,_,_,_,4,_,_,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [3,_,_,_,_,9,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,4,_,_,4,_,4,4,_,8,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,4,9,9,4,_,_,_,_,7,_,2],
    [3,_,_,_,_,8,_,_,_,_,_,4,_,_,4,_,_,_,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [3,_,_,_,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,8,_,2],
    [7,7,7,7,7,7,7,7,7,8,7,7,7,7,_,_,_,_,_,7,_,2],
    [9,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,8,_,2],
    [7,_,_,_,_,7,7,7,7,8,7,7,7,7,7,7,9,7,7,7,_,2],
    [7,_,_,_,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [7,_,4,4,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [7,_,_,_,_,7,_,_,_,4,5,_,_,4,4,_,_,_,_,7,_,2],
    [8,_,_,_,_,7,_,_,_,_,4,_,_,5,_,_,_,_,_,7,_,2],
    [8,_,4,5,_,7,_,_,_,_,_,_,_,_,_,_,_,_,_,7,_,2],
    [7,_,_,_,_,7,_,_,_,7,7,7,7,7,7,7,_,_,_,7,_,2],
    [7,_,_,_,_,7,_,_,_,7,1,_,_,_,_,_,_,_,_,7,_,2],
    [9,_,_,_,_,7,_,_,_,7,1,_,_,_,_,_,_,_,_,7,_,2],
    [7,_,5,4,_,7,_,_,_,9,1,_,_,_,1,7,7,7,7,7,_,2],
    [7,_,_,_,_,_,_,_,_,7,1,_,_,_,1,_,_,_,_,4,_,2],
    [7,_,_,_,_,_,_,_,_,7,1,_,_,_,1,_,_,_,_,4,_,2],
    [7,7,8,8,7,7,7,7,9,7,1,_,_,_,1,_,_,_,_,4,_,2],
    [7,7,7,7,7,7,_,_,_,_,8,_,_,_,8,_,_,_,_,4,_,2],
    [4,_,_,_,_,4,_,_,_,_,1,_,_,_,1,_,_,_,_,4,_,2],
    [4,_,_,_,_,4,_,_,_,_,1,_,_,_,1,_,_,_,_,7,_,2],
    [4,_,_,_,_,1,1,1,4,5,1,_,_,_,1,6,4,1,1,7,_,2],
    [3,_,_,_,_,9,_,_,_,_,_,_,_,_,_,_,_,_,_,9,_,2],
    [3,_,_,_,_,9,_,_,_,_,_,_,_,_,_,_,_,_,_,9,_,2],
    [3,_,_,_,_,1,1,_,_,4,4,9,8,9,4,4,_,_,1,1,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,2],
    [3,_,_,_,_,6,_,_,_,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,2],
    [3,_,_,_,_,5,_,_,_,4,4,5,_,5,4,4,_,_,_,1,_,2],
    [3,_,_,_,_,4,_,_,_,_,_,5,_,5,_,_,_,_,_,1,_,2],
    [3,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,5,_,2],
    [3,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,4,_,2],
    [3,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,2],
    [3,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,2],
    [3,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,2],
    [3,_,_,_,_,1,1,1,1,1,1,8,9,8,1,1,1,1,1,1,_,2],
    [3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2],
    [3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2],
    [3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2],
    [3,1,2,3,2,3,1,3,2,2,1,2,1,3,3,3,2,3,1,1,2,1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        #self.rows = len(self.mini_map)
        #self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) 
        for pos in self.world_map]
