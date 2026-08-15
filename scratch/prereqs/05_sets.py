# beat 1 - set in, sorted list out
def unique(items):
    return sorted(set(items))


assert unique([3, 1, 3, 2, 1]) == [1, 2, 3]
assert unique([]) == []
assert unique([10, 3, 7, 3]) == [3, 7, 10]


# beat 2 - intersection
def common(a, b):
    return set(a) & set(b)

assert common([1, 2, 3], [2, 3, 4]) == {2, 3}
assert common([1], [2]) == set()


# beat 3 - difference
def only_in_first(a, b):
    return set(a) - set (b)


assert only_in_first([1, 2, 3], [2, 3, 4]) == {1}
assert only_in_first([1, 2], [1, 2]) == set()


# beat 4 - an actual bool, not a count
def has_duplicates(items):
    return len(items) != len(set(items))

assert has_duplicates([1, 2, 1]) is True
assert has_duplicates([1, 2, 3]) is False


# beat 5 - the values appearing more than once
def duplicates(items):
    a = []
    for n in items:
        if items.count(n) > 1:
            a.append(n)
    return set(a)


assert duplicates([1, 2, 2, 3, 3, 3]) == {2, 3}
assert duplicates([1, 2, 3]) == set()

print("05 passed")
