# given - the ordinary class, for contrast
class Loose:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# beat 1 - the same class with __slots__
class Point:
    raise NotImplementedError


p = Point(1, 2)
assert p.x == 1
assert p.y == 2

p.x = 10
assert p.x == 10

assert hasattr(Loose(1, 2), "__dict__") is True
assert hasattr(p, "__dict__") is False

try:
    p.z = 3
except AttributeError:
    pass
else:
    raise AssertionError("setting p.z should have raised AttributeError")

assert set(Point.__slots__) == {"x", "y"}

print("10 passed")
