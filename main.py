import pyxel

from Class.Snake import Snake
from Class.Fruit import Fruit


class App:
    def __init__(self):
        pyxel.init(128, 128, title="Jeu")
        pyxel.load("snake.pyxres")

        self.snake = Snake([64, 64], [0, -8], True)
        self.snake.grow()
        self.fruit = Fruit()

        self.dir_change = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % 15 == 0:
            self.snake.move()
            self.dir_change = False
        if self.snake.on_wall() or self.snake.on_tail(self.snake.pos):
            quit_app()
        if not self.dir_change:
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.snake.change_direction([-self.snake.direction[1], self.snake.direction[0]])
                self.dir_change = True
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.snake.change_direction([self.snake.direction[1], -self.snake.direction[0]])
                self.dir_change = True
        if self.snake.pos == self.fruit.pos:
            self.snake.grow()
            self.fruit.pos = None
        if self.fruit.pos is None:
            self.fruit.spawn(self.snake)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        self.snake.draw()
        self.fruit.draw()


def quit_app():
    pyxel.quit()


App()
