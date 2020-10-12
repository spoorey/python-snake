import tkinter
import tkinter.messagebox
import threading

from GameSettings import GameSettings
from GameState import GameState
from PlayerSnake import PlayerSnake
from TKRenderer import TKRenderer

settings = GameSettings()
state = GameState(settings, PlayerSnake(settings))

top = tkinter.Tk()

def keyPress(event):
    key = event.keysym.lower()
    if key in ['right', 'left', 'up', 'down']:
        if not (
        (key == 'right' and state.snake.direction == 'left')
        or (key == 'left' and state.snake.direction == 'right')
        or (key == 'down' and state.snake.direction == 'up')
        or (key == 'up' and state.snake.direction == 'down')):
            state.snake.newDirection = key

    if (event.keysym == 'space'):
        state.snake.availableFood += 1


def render(renderer: TKRenderer):
    renderer.render(state)
    threading.Timer(1/settings.framesPerSecond, render, [renderer]).start()

def tick():
    state.tick()
    threading.Timer(1/settings.ticksPerSecond, tick).start()

render(TKRenderer(settings, top))
tick()

top.bind('<Key>', keyPress)
top.mainloop()
