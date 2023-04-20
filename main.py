import pyxel

from Class.Snake import Snake
from Class.Fruit import Fruit


class App:
    def __init__(self):
        pyxel.init(128, 128, title="Jeu")
        pyxel.load("snake.pyxres")

        self.snake = Snake([64, 64], [0, -8], True)
        self.fruit = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % 120 == 0:
            self.snake.grow()
        if pyxel.frame_count % 30 == 0:
            self.snake.move()
        if self.snake.on_wall():
            quit_app()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        self.snake.draw()


def quit_app():
    pyxel.quit()


App()
