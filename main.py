import tkinter
import tkinter.messagebox
import threading

from GameSettings import GameSettings
from PlayerSnake import PlayerSnake
from TKRenderer import TKRenderer

settings = GameSettings()
snake = PlayerSnake(settings)

top = tkinter.Tk()

def keyPress(event):
    if event.keysym.lower() in ['right', 'left', 'up', 'down']:
        snake.direction = event.keysym.lower()

    if (event.keysym == 'space'):
        snake.availableFood += 1


def render(renderer: TKRenderer):
    threading.Timer(0.2, render, [renderer]).start()
    if (snake.bitesItSelf() or snake.bitesEdge()):
        print('nooo')
        snake.reset(10)
    renderer.render(snake)

    snake.move()


render(TKRenderer(settings, top))
top.bind('<Key>', keyPress)
top.mainloop()
