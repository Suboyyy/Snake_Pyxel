import pyxel


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
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.snake.change_direction([-self.snake.direction[1], self.snake.direction[0]])
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.snake.change_direction([self.snake.direction[1], -self.snake.direction[0]])
        if self.snake.on_wall():
            quit_app()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        self.snake.draw()


class Snake:
    def __init__(self, pos, direction, head):
        self.pos = pos
        self.direction = direction
        self.next = None
        self.head = head

    def __str__(self):
        return f"Ce serpent a sa tête en {self.pos}, va en direction {self.direction} et est de taille {self.lenght()}"

    def lenght(self):
        if self.next is None:
            return 1
        return self.next.lenght() + 1

    def move(self, dir_before=None):
        self.pos = [self.pos[x] + self.direction[x] for x in range(2)]
        temp_dir = self.direction
        if dir_before is not None:
            self.direction = dir_before
        if self.next is not None:
            self.next.move(temp_dir)

    def change_direction(self, direction):
        self.direction = direction

    def grow(self):
        if self.next is not None:
            self.next.grow()
        else:
            pos = [self.pos[x] - self.direction[x] for x in range(2)]
            self.next = Snake(pos, self.direction, False)

    def draw(self):
        if self.head:
            pyxel.blt(self.pos[0], self.pos[1], 0, 32 + self.direction[0] + self.direction[1] * 2, 16, 8, 8, 2)
        else:
            pyxel.blt(self.pos[0], self.pos[1], 0, 32 + self.direction[0] + self.direction[1] * 2, 24, 8, 8, 2)
        if self.next is not None:
            self.next.draw()

    def on_wall(self):
        return 0 > self.pos[0] or self.pos[0] > 127 or 0 > self.pos[1] or self.pos[1] > 127


def quit_app():
    pyxel.quit()


App()
