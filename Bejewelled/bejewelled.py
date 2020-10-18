import random
from datetime import datetime

random.seed(datetime.now())

class game:
    def __init__(gridSize):
        gameGrid[gridSize][gridSize]
        for x in range(gridSize):
            for y in range(gridSize):
                gridSize[x][y] = random.randind(range(0,3))
    
    def drawGrid(gridSize):
        for x in range(gridSize):
            for y in range(gridSize):
                print(gameGrid[x][y])

gridSize = 10
game.__init__(gridSize)
game.drawGrid(gridSize)