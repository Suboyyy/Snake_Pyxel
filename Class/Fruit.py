from random import randint

import pyxel


class Fruit:
    def __init__(self):
        self.image = [8, 0]
        self.pos = None

    def spawn(self, snake):
        if self.pos is None:
            while True:
                can_spawn = False
                pos = [8 * randint(0, 16), 8 * randint(0, 16)]
                while snake.next is not None:
                    if snake.pos == pos:
                        pass
                    else:
                        can_spawn = True
                if can_spawn:
                    break
            self.pos = pos
