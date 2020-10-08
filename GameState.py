import GameSettings
import PlayerSnake
import random

class GameState:
    def __init__(self, settings: GameSettings, snake: PlayerSnake):
        self.settings = settings
        self.snake = snake
        self.foodCoordinates = []

    def tick(self):
        snake = self.snake
        if self.__snakeBitesItSelf() or self.__snakeBitesEdge():
            snake.reset()

        for index, food in enumerate(self.foodCoordinates):
            if self.__snakeBites(food[0], food[1]):
                self.snake.availableFood += 1
                self.foodCoordinates.pop(index)

        if len(self.foodCoordinates) < self.settings.maxFoods:
            self.createFood()

        snake.move()

    def coordinateIsFree(self, x, y):
        if self.snakeTouches(x, y):
            return False

        for coordinate in self.foodCoordinates:
            if coordinate[0] == x and coordinate[1] == y:
                return False

        return True

    def createFood(self):
        while True:
            x = random.randint(0, self.settings.gridWidth - 1)
            y = random.randint(0, self.settings.gridHeight - 1)
            if self.coordinateIsFree(x, y):
                break

        self.foodCoordinates.append([x, y])


    def snakeTouches(self, x, y):
        for id, coordinate in enumerate(self.snake.bodyCoordinates):
            if (
                (id < len(self.snake.bodyCoordinates) - 1) and
                (coordinate[0] == x) and
                (coordinate[1] == y)
            ):
                return True

        return False

    def __snakeBites(self, x, y):
        return self.snake.headX == x and self.snake.headY == y

    def __snakeBitesItSelf(self):
        return self.snakeTouches(self.snake.headX, self.snake.headY)

    def __snakeBitesEdge(self):
        return not self.settings.isInArea(self.snake.headX, self.snake.headY)