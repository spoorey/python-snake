import GameSettings

class PlayerSnake:
    direction='right'
    headX = 10
    headY = 10
    bodyCoordinates = []
    availableFood = 0
    settings = 0

    def __init__(self, settings: GameSettings):
        self.reset(10)
        self.settings = settings

    def reset(self, snakeLength: int):
        self.direction = 'right'
        self.bodyCoordinates = []
        self.headX = 10
        self.headY = 10
        i = 0
        while i < snakeLength:
            i += 1
            self.headX += 1
            self.bodyCoordinates.append([self.headX, self.headY])
        self.move()

    def move(self):
        if (self.direction == 'right'):
            self.headX += 1
        elif (self.direction == 'left'):
            self.headX -= 1
        elif (self.direction == 'down'):
            self.headY += 1
        else:
            self.headY -= 1
        self.bodyCoordinates.append([self.headX, self.headY])
        if (self.availableFood >= 1):
            self.availableFood -= 1
        else:
            self.bodyCoordinates.pop(0)
    def bitesItSelf(self):
        for id, coordinate in enumerate(self.bodyCoordinates):
            if (
                (id < len(self.bodyCoordinates) - 1) and
                (coordinate[0] == self.headX) and
                (coordinate[1] == self.headY)
            ):
                return True

        return False

    def bitesEdge(self):
        return not self.settings.isInArea(self.headX, self.headY)