class GameSettings:
    def __init__(self):
        self.ticksPerSecond = 2
        self.framesPerSecond = 30
        self.gridHeight = 15
        self.gridWidth = 15
        self.maxFoods = self.gridWidth*self.gridHeight / 50

    def isInArea(self, x: int, y: int):
        xFits = (x >= 0) and (x < self.gridWidth)
        yFits = (y >= 0) and (y < self.gridHeight)

        return xFits and yFits