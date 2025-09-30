

from vector2d import Vector2D, clamp

class Paddle:
    def __init__(self, pos, size, velocity, total_w=640, total_h=480):
        self.p, self.size, self.v = pos, size, velocity
        self.direction = Vector2D(0, 0)
        self.total_w, self.total_h = total_w, total_h

    def move(self):
        # WRITE YOUR CODE HERE       

    def get_sizes(self): 
        # WRITE YOUR CODE HERE

    def get_velocity(self): 
        return self.v * self.direction


if __name__ == "__main__":
    block = Paddle(Vector2D(400, 200), Vector2D(20, 20), 100)
    assert isinstance(block, Paddle), "Not an instance of Paddle"
    p, sz = block.get_sizes()
    assert p.x == 400 and p.y == 200, "Coordinates not set properly"
    assert sz.x == 20 and sz.y == 20, "Width/Height not set properly"
    block.direction = Vector2D(-1, 1)
    block.move()
    p, sz = block.get_sizes()
    assert p.x == 300 and p.y == 300, "Coordinates not set properly"
    assert sz.x == 20 and sz.y == 20, "Width/Height not set properly"
    print("TESTS PASSED")