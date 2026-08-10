import itertools


# beat 1 - split, reverse, join
def reverse_words(sentence):
    raise NotImplementedError


assert reverse_words("the cat sat") == "sat cat the"
assert reverse_words("hi") == "hi"


# beat 2 - itertools.chain.from_iterable
def flattened(nested):
    raise NotImplementedError


assert flattened([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
assert flattened([[1], [], [2, 3]]) == [1, 2, 3]
assert flattened([]) == []


# beat 3 - slicing with a negative step
def is_palindrome(text):
    raise NotImplementedError


assert is_palindrome("racecar") is True
assert is_palindrome("Racecar") is True
assert is_palindrome("hello") is False


# beat 4 - merge two dicts without mutating either
def merged(a, b):
    raise NotImplementedError


left = {"x": 1, "y": 2}
right = {"y": 99, "z": 3}
assert merged(left, right) == {"x": 1, "y": 99, "z": 3}
assert left == {"x": 1, "y": 2}


# beat 5 - a comprehension slicing over a stepped range
def chunk(items, size):
    raise NotImplementedError


assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert chunk([], 3) == []

print("20 passed")
