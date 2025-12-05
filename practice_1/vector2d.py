
import math

class Vector2D:
    def __init__(self, x=0, y=0): 
        self.x, self.y = x, y

    def __add__(self, other): 
        # REMOVE pass and WRITE YOUR CODE HERE
        pass
    
    def __sub__(self, other): 
        # REMOVE pass and WRITE YOUR CODE HERE
        pass

    def __mul__(self, num): 
        # REMOVE pass and WRITE YOUR CODE HERE
        pass

    def __rmul__(self, num): 
        return self.__mul__(num)

    def __truediv__(self, num): 
        return self.__mul__(1.0 / num)

    def dot(self, other): 
        # REMOVE pass and WRITE YOUR CODE HERE
        pass

    def perp(self):
        # REMOVE pass and WRITE YOUR CODE HERE
        pass

    def lng(self): 
        # REMOVE pass and WRITE YOUR CODE HERE
        pass

    def decompose(self, other):
        # REMOVE pass and WRITE YOUR CODE HERE
        pass

def clamp(x, x_min, x_max):
    # REMOVE pass and WRITE YOUR CODE HERE
    pass


if __name__ == "__main__":
    v = Vector2D(1, 2)
    assert isinstance(v, Vector2D), "Not instance of Vector2D"
    assert v.x == 1 and v.y == 2, "Attribute 'x' or 'y' is incorrect"
    u = 3 * v
    w = v * 5
    assert u.x == 3 and u.y == 6 and w.x == 5 and w.y == 10, "Wrong multilication"
    t = v / 2
    assert t.x == 0.5 and t.y == 1, "Wrong division"
    s = u + w
    assert s.x == 8 and s.y == 16, "Wrong addition"
    v = w - u
    assert v.x == 2 and v.y == 4, "Wrong subtraction"
    v = Vector2D(1, 2)
    u = Vector2D(3, 4)
    p1 = v.dot(u)
    p2 = u.dot(v)
    assert p1 == 11 and p2 == 11, "Wrong dot product"
    p = v.perp()
    assert p.x == -2 and p.y == 1, "Wrong perpendicular"
    l = u.lng()
    assert l == 5, "Wrong vector length"
    v = Vector2D(3, 4)
    u = Vector2D(1, 0)
    v1, v2 = v.decompose(u)
    assert v1.x == 3 and v1.y == 0 and v2.x == 0 and v2.y == 4, "Wrong decomposition"
    print("VECTOR TESTS SUCCESSFULLY PASSED")

    assert clamp(1, 3, 7) == 3, "clamp lower bound error"
    assert clamp(5, 3, 7) == 5, "clamp intermediate error"
    assert clamp(14, 3, 7) == 7, "clamp upper bound error"
    print("CLAMP TESTS SUCCESSFULLY PASSED")