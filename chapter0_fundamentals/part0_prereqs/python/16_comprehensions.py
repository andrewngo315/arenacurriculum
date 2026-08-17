# beat 1 - list comprehension with a filter
def even_squares(nums):
    return [i ** 2 for i in nums if i % 2 == 0]
    

assert even_squares([1, 2, 3, 4]) == [4, 16]
assert even_squares([1, 3]) == []


# beat 2 - dict comprehension
def word_lengths(words):
    return {f"{w}": len(w) for w in words}


assert word_lengths(["hi", "there"]) == {"hi": 2, "there": 5}
assert word_lengths([]) == {}


# beat 3 - set comprehension
def initials(names):
    return {f"{n[0]}" for n in names}


assert initials(["ann", "bob", "amy"]) == {"a", "b"}
assert initials([]) == set()
assert initials(["zoe", "zed", "kim"]) == {"z", "k"}


# beat 4 - nested, two fors
def flatten(rows):
    return [x for row in rows for x in row]


assert flatten([[1, 2], [3], []]) == [1, 2, 3]
assert flatten([]) == []


# beat 5 - nested with both indices. rows may be ragged
def labelled(grid):
    return [(vector, position, number) for vector, numbers in enumerate(grid) for position, number in enumerate(numbers)]


assert labelled([[1, 2], [3, 4]]) == [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4)]
assert labelled([[1, 2, 3]]) == [(0, 0, 1), (0, 1, 2), (0, 2, 3)]
assert labelled([[1], [2, 3]]) == [(0, 0, 1), (1, 0, 2), (1, 1, 3)]
assert labelled([]) == []


# beat 6 - round brackets make a generator, not a list
def squares_gen(nums):
    return (n ** 2 for n in nums)
    


g = squares_gen([1, 2, 3])
assert type(g).__name__ == "generator"
assert next(g) == 1
assert list(g) == [4, 9]
assert list(g) == []

print("16 passed")
