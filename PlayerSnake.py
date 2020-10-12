import GameSettings

class PlayerSnake:
    direction='right'
    headX = 10
    headY = 10
    bodyCoordinates = []
    availableFood = 0
    settings = 0
    newDirection = ''

    def __init__(self, settings: GameSettings):
        self.settings = settings
        self.reset()

    def reset(self):
        self.direction = 'right'
        self.bodyCoordinates = []
        self.headX = 0
        self.headY = 1
        i = 0
        while i < 5:
            i += 1
            self.headX += 1
            self.bodyCoordinates.append([self.headX, self.headY])

    def move(self):
        if (self.newDirection != ''):
            self.direction = self.newDirection
            self.newDirection = ''

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