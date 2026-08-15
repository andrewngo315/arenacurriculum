# beat 1 - read only. zip is a lazy iterator, not a list
assert list(zip([1, 2], [3])) == [(1, 3)]
assert zip([1], [2]) != [(1, 2)]


# beat 2 - zip truncates to the shorter input
def to_dict(keys, values):
    raise NotImplementedError


assert to_dict(["a", "b"], [1, 2]) == {"a": 1, "b": 2}
assert to_dict([], []) == {}
assert to_dict(["a", "b"], [1]) == {"a": 1}


# beat 3 - zip(*pairs), but read the assert for the shape it wants
def unzip(pairs):
    raise NotImplementedError


assert unzip([(1, "a"), (2, "b")]) == ([1, 2], ["a", "b"])
assert unzip([]) == ([], [])


# beat 4 - walk two lists in step
def dot(a, b):
    raise NotImplementedError


assert dot([1, 2, 3], [4, 5, 6]) == 32
assert dot([0], [7]) == 0


# beat 5 - same, elementwise
def pairwise_max(a, b):
    raise NotImplementedError


assert pairwise_max([1, 5, 3], [4, 2, 3]) == [4, 5, 3]
assert pairwise_max([9, 1], [2, 8]) == [9, 8]
assert pairwise_max([1, 5, 3], [4]) == [4]
assert pairwise_max([], []) == []

print("14 passed")
