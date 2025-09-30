

from vector2d import Vector2D, clamp

class Ball:
    def __init__(self, radius, pos, velocity, gravity=0.0, clamp_v=True):
        self.r = radius
        self.p, self.v = pos, velocity
        self.g, self.clamp = gravity, clamp_v

    def move(self):
        # WRITE YOUR CODE HERE

    def check_collision_and_bounce(self, A, B):
        # WRITE YOUR CODE HERE

    def add_to_velocity(self, v):
        self.v += v

    def get_coordinates(self): 
        # WRITE YOUR CODE HERE

    def get_properties(self): 
        # WRITE YOUR CODE HERE


if __name__ == "__main__":
    ball = Ball(15, Vector2D(10, 15), Vector2D(-1, 1), 0.0)
    assert isinstance(ball, Ball), "Not an instance of Ball"
    p = ball.get_coordinates()
    assert p.x == 10 and p.y == 15, "Coordinates not set properly"
    ball.move()
    p = ball.get_coordinates()
    assert p.x == 9 and p.y == 16, "Moves incorrectly"
    r = ball.get_properties()
    assert r == 15 , "Properties are wrong"
    ball = Ball(2, Vector2D(0, 0), Vector2D(1, -1), 10.0)
    for _ in range(100):
      ball.move()
    p = ball.get_coordinates()
    assert 99 < p.x < 101 and -101 < p.y < -99, "Velocity not clamped"

    b = Ball(10, Vector2D(10, 0), Vector2D(5, 0), 0.0)
    was_collision = False
    for _ in range(10):
      b.move()
      if b.check_collision_and_bounce(Vector2D(25, 10), Vector2D(25, -10)): was_collision = True
    if not was_collision:
      assert False, "No collision reported (function should have returned true at some point)"
    p = b.get_coordinates()
    assert p.y == 0, "y coordinate should not change during x-bounce"
    assert p.x < 0, "did not bounce (vertical, bounce from the left)"

    b = Ball(10, Vector2D(-10, 0), Vector2D(-5, 0), 0.0)
    was_collision = False
    for _ in range(10):
      b.move()
      if b.check_collision_and_bounce(Vector2D(-25, 10), Vector2D(-25, -10)): was_collision = True
    if not was_collision:
      assert False, "No collision reported (function should have returned true at some point)"
    p = b.get_coordinates()
    assert p.y == 0, "y coordinate should not change during x-bounce"
    assert p.x > 0, "did not bounce (vertical, bounce from the right)"

    b = Ball(10, Vector2D(0,10), Vector2D(0,5), 0.0)
    was_collision = False
    for _ in range(10):
      b.move()
      if b.check_collision_and_bounce(Vector2D(10, 25), Vector2D(-10, 25)): was_collision = True
    if not was_collision:
      assert False, "No collision reported (function should have returned true at some point)"
    p = b.get_coordinates()
    assert p.x == 0, "x coordinate should not change during y-bounce"
    assert p.y < 0, "did not bounce (horizontal, bounce from below)"

    b = Ball(10, Vector2D(0,-10), Vector2D(0,-5), 0.0)
    was_collision = False
    for _ in range(10):
      b.move()
      if b.check_collision_and_bounce(Vector2D(10, -25), Vector2D(-10, -25)): was_collision = True
    if not was_collision:
      assert False, "No collision reported (function should have returned true at some point)"
    p = b.get_coordinates()
    assert p.x == 0, "x coordinate should not change during y-bounce"
    assert p.y > 0, "did not bounce (horizontal, bounce from above)"

    print("TESTS PASSED")