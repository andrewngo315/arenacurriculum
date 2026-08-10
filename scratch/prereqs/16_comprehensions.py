# beat 1 - list comprehension with a filter
def even_squares(nums):
    raise NotImplementedError


assert even_squares([1, 2, 3, 4]) == [4, 16]
assert even_squares([1, 3]) == []


# beat 2 - dict comprehension
def word_lengths(words):
    raise NotImplementedError


assert word_lengths(["hi", "there"]) == {"hi": 2, "there": 5}
assert word_lengths([]) == {}


# beat 3 - set comprehension
def initials(names):
    raise NotImplementedError


assert initials(["ann", "bob", "amy"]) == {"a", "b"}
assert initials([]) == set()
assert initials(["zoe", "zed", "kim"]) == {"z", "k"}


# beat 4 - nested, two fors
def flatten(rows):
    raise NotImplementedError


assert flatten([[1, 2], [3], []]) == [1, 2, 3]
assert flatten([]) == []


# beat 5 - nested with both indices. rows may be ragged
def labelled(grid):
    raise NotImplementedError


assert labelled([[1, 2], [3, 4]]) == [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4)]
assert labelled([[1, 2, 3]]) == [(0, 0, 1), (0, 1, 2), (0, 2, 3)]
assert labelled([[1], [2, 3]]) == [(0, 0, 1), (1, 0, 2), (1, 1, 3)]
assert labelled([]) == []


# beat 6 - round brackets make a generator, not a list
def squares_gen(nums):
    raise NotImplementedError


g = squares_gen([1, 2, 3])
assert type(g).__name__ == "generator"
assert next(g) == 1
assert list(g) == [4, 9]
assert list(g) == []

print("16 passed")
