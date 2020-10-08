import PlayerSnake
import GameSettings
from tkinter import Canvas
import tkinter

from GameState import GameState

class TKRenderer:
    def __init__(self, settings: GameSettings, top: tkinter.Tk):
        self.settings = settings
        self.canvas = Canvas(top, bg='#cccccc', height=settings.windowHeight, width=settings.windowWidth)

        self.canvas.pack()
        self.gridLines = []
        self.snakeParts = []
        self.renderGrid()

    def renderSnake(self, snake: PlayerSnake):
        for part in self.snakeParts:
            self.canvas.delete(part)

        for coordinate in snake.bodyCoordinates:
            self.snakeParts.append(self.fillSquare(coordinate[0], coordinate[1], '#0000ff'))

    def renderGrid(self):
        settings = self.settings
        canvas = self.canvas
        for line in self.gridLines:
            canvas.delete(line)

        x = settings.squareSideLength
        y = settings.squareSideLength

        while x < settings.windowWidth:
            self.gridLines.append(canvas.create_line(x, 0, x, settings.windowHeight))
            x += settings.squareSideLength

        while y < settings.windowHeight:
            self.gridLines.append(canvas.create_line(0, y, settings.windowWidth, y))
            y += settings.squareSideLength

    def render(self, state: GameState):
        self.renderSnake(state.snake)

    def fillSquare(self, x, y, color):
        settings = self.settings

        return self.canvas.create_rectangle(
            x * settings.squareSideLength,
            y * settings.squareSideLength,
            (x + 1) * settings.squareSideLength,
            (y + 1) * settings.squareSideLength,
            fill=color
        )
