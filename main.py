import tkinter

from PlayerSnake import PlayerSnake

top = tkinter.Tk()

class GameSettings:
    squareSideLength = 10
    windowHeight = 1000
    windowWidth = 1000

def keyPress(event):
    if (event.keysym.lower() in ['right', 'left', 'up', 'down']):
        PlayerSnake.direction = event.keysym.lower()
    
    if (event.keysym == 'space'):
        PlayerSnake.availableFood += 1

def fillSquare(canvas, x, y, color):
    canvas.create_rectangle(
        x*GameSettings.squareSideLength,
        y*GameSettings.squareSideLength,
        (x+1)*GameSettings.squareSideLength,
        (y+1)*GameSettings.squareSideLength,
        fill=color
)

def render(top, canvas):
    canvas.delete('all')
    top.after(200, render, top, canvas)

    x = GameSettings.squareSideLength
    y = GameSettings.squareSideLength

    while (x < GameSettings.windowWidth):
        canvas.create_line(x, 0, x, GameSettings.windowHeight)
        x += GameSettings.squareSideLength

    while (y < GameSettings.windowHeight):
        canvas.create_line(0, y, GameSettings.windowWidth, y)
        y += GameSettings.squareSideLength

    for coordinate in PlayerSnake.bodyCoordinates:
        fillSquare(canvas, coordinate[0], coordinate[1], '#0000ff')
    PlayerSnake.move()

PlayerSnake.reset(10)
canvas = tkinter.Canvas(top, bg='#cccccc', height=GameSettings.windowHeight, width=GameSettings.windowWidth)
canvas.pack()
render(top, canvas)
top.bind('<Key>', keyPress)
top.mainloop()
