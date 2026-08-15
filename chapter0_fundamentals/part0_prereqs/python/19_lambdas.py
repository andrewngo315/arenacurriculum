# beat 1 - a lambda assigned to a name
add = None
if add is None:
    raise NotImplementedError
assert callable(add)
assert add(2, 3) == 5
assert add(0, 0) == 0
assert add(-4, 10) == 6


people = [("bob", 30), ("ann", 25), ("cat", 41)]


# beat 2 - sorted with a lambda key, without reordering the caller's list
def by_age(records):
    raise NotImplementedError


assert by_age(people) == [("ann", 25), ("bob", 30), ("cat", 41)]
assert people == [("bob", 30), ("ann", 25), ("cat", 41)]


# beat 3 - the key function passed in as an argument
def sort_by(items, key):
    raise NotImplementedError


assert sort_by(["ccc", "a", "bb"], len) == ["a", "bb", "ccc"]
assert sort_by([-3, 1, -2], abs) == [1, -2, -3]


# beat 4 - a lambda closing over n
def make_adder(n):
    raise NotImplementedError


add_five = make_adder(5)
assert add_five(10) == 15
assert make_adder(0)(7) == 7


# beat 5 - a dict of lambdas
operations = None
if operations is None:
    raise NotImplementedError
assert operations["double"](4) == 8
assert operations["square"](4) == 16
assert operations["negate"](4) == -4
assert operations["double"](0) == 0
assert operations["square"](3) == 9
assert operations["negate"](-7) == 7
assert sorted(operations) == ["double", "negate", "square"]

print("19 passed")
