import pyxel


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
        if self.next is not None:
            self.next.move()
        self.pos = [self.pos[x] + self.direction[x] for x in range(2)]
        """temp_dir = self.direction
        if dir_before is not None:
            self.direction = dir_before
        if self.next is not None:
            self.next.move(temp_dir)"""

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
