from random import randint

import pyxel


class Fruit:
    def __init__(self):
        self.image = [16, 0]
        self.pos = None

    def spawn(self, snake):
        if self.pos is None:
            while True:
                can_spawn = False
                pos = [8 * randint(0, 15), 8 * randint(0, 15)]
                while snake is not None:
                    if snake.pos == pos:
                        can_spawn = False
                        break
                    else:
                        can_spawn = True
                    snake = snake.next
                if can_spawn:
                    break
            self.pos = pos

    def draw(self):
        pyxel.blt(self.pos[0], self.pos[1], 0, self.image[0], self.image[1], 8, 8, 2)

    def delete(self):
        self.pos = None
