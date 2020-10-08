class GameSettings:
    squareSideLength = 10
    windowHeight = 1000
    windowWidth = 1000
    ticksPerSecond = 3
    framesPerSecond = 3

    def isInArea(self, x: int, y: int):
        xFits = (x >= 0) and (x < self.windowWidth/self.squareSideLength)
        yFits = (y >= 0) and (y < self.windowWidth/self.squareSideLength)

        return xFits and yFits