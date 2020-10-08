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
    if event.keysym.lower() in ['right', 'left', 'up', 'down']:
        state.snake.direction = event.keysym.lower()

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
