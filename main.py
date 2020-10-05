import tkinter

from GameSettings import GameSettings
from PlayerSnake import PlayerSnake

settings = GameSettings()
snake = PlayerSnake(settings)

top = tkinter.Tk()

def keyPress(event):
    if event.keysym.lower() in ['right', 'left', 'up', 'down']:
        snake.direction = event.keysym.lower()
    
    if (event.keysym == 'space'):
        snake.availableFood += 1

def fillSquare(canvas, x, y, color):
    canvas.create_rectangle(
        x * settings.squareSideLength,
        y * settings.squareSideLength,
        (x+1) * settings.squareSideLength,
        (y+1) * settings.squareSideLength,
        fill=color
)

def render(top, canvas):
    canvas.delete('all')
    top.after(200, render, top, canvas)

    x = settings.squareSideLength
    y = settings.squareSideLength
    snake.bitesItSelf()
    snake.bitesEdge()

    while (x < settings.windowWidth):
        canvas.create_line(x, 0, x, settings.windowHeight)
        x += settings.squareSideLength

    while (y < settings.windowHeight):
        canvas.create_line(0, y, settings.windowWidth, y)
        y += settings.squareSideLength

    for coordinate in snake.bodyCoordinates:
        fillSquare(canvas, coordinate[0], coordinate[1], '#0000ff')
    snake.move()

canvas = tkinter.Canvas(top, bg='#cccccc', height=settings.windowHeight, width=settings.windowWidth)
canvas.pack()
render(top, canvas)
top.bind('<Key>', keyPress)
top.mainloop()
