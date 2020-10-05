class GameSettings:
    squareSideLength = 10
    windowHeight = 1000
    windowWidth = 1000
    def isInArea(x: int, y: int):
        xFits = (x >= 0) and (x < GameSettings.windowWidth/GameSettings.squareSideLength)
        yFits = (y >= 0) and (y < GameSettings.windowWidth/GameSettings.squareSideLength)

        return xFits and yFits