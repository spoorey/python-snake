import GameSettings
import PlayerSnake

class GameState:
    def __init__(self, settings: GameSettings, snake: PlayerSnake):
        self.settings = settings
        self.snake = snake

    def tick(self):
        snake = self.snake
        if self.__snakeBitesItSelf() or self.__snakeBitesEdge():
            print('nooo')
            snake.reset(10)
        snake.move()

    def __snakeBitesItSelf(self):
        for id, coordinate in enumerate(self.snake.bodyCoordinates):
            if (
                (id < len(self.snake.bodyCoordinates) - 1) and
                (coordinate[0] == self.snake.headX) and
                (coordinate[1] == self.snake.headY)
            ):
                return True

        return False

    def __snakeBitesEdge(self):
        return not self.settings.isInArea(self.snake.headX, self.snake.headY)