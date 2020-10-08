import PlayerSnake
import GameSettings
from tkinter import Canvas
import tkinter

from GameState import GameState

class TKRenderer:
    def __init__(self, settings: GameSettings, top: tkinter.Tk):
        self.settings = settings
        self.squareSide = 30
        self.windowHeight = settings.gridHeight * self.squareSide
        self.windowWidth = settings.gridWidth * self.squareSide
        self.gridLines = []
        self.snakeParts = []
        self.foods = []

        self.canvas = Canvas(top, bg='#cccccc', height=self.windowHeight, width=self.windowWidth)
        self.canvas.pack()

        self.renderGrid()

    def render(self, state: GameState):
        for food in self.foods:
            self.canvas.delete(food)

        for food in state.foodCoordinates:
            self.foods.append(self.fillSquare(food[0], food[1], '#ff0000'))

        self.renderSnake(state.snake)

    def renderSnake(self, snake: PlayerSnake):
        for part in self.snakeParts:
            self.canvas.delete(part)


        for coordinate in snake.bodyCoordinates:
            self.snakeParts.append(self.fillSquare(coordinate[0], coordinate[1], '#0000ff'))

        self.snakeParts.append(self.fillSquare(snake.headX, snake.headY, '#00ffff'))

    def renderGrid(self):
        canvas = self.canvas
        for line in self.gridLines:
            canvas.delete(line)

        squareSideLength = self.squareSide
        windowWidth = self.windowWidth
        windowHeight = self.windowHeight

        x = squareSideLength
        y = squareSideLength

        while x < windowWidth:
            self.gridLines.append(canvas.create_line(x, 0, x, windowHeight))
            x += squareSideLength

        while y < windowHeight:
            self.gridLines.append(canvas.create_line(0, y, windowWidth, y))
            y += squareSideLength


    def fillSquare(self, x, y, color):
        return self.canvas.create_rectangle(
            x * self.squareSide,
            y * self.squareSide,
            (x + 1) * self.squareSide,
            (y + 1) * self.squareSide,
            fill=color
        )
