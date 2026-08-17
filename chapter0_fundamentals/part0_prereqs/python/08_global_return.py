hits = 0


# beat 1 - rebinding a module-level name needs global
def record_hit():
    global hits
    hits = hits + 1


record_hit()
record_hit()
assert hits == 2
record_hit()
assert hits == 3


shots = 0


# beat 2 - the same body without global. read what it does instead
def record_shot_wrong():
    return 1


assert record_shot_wrong() == 1
assert shots == 0


# beat 3 - reading a module-level name needs no global at all
def current_hits():
    return hits


assert current_hits() == 3


# beat 4 - return a tuple, and unpack it
def min_max(nums):
    list = sorted(nums)
    min = list[0]
    max = list[-1]
    return min, max

assert min_max([3, 1, 4]) == (1, 4)
assert min_max([7]) == (7, 7)

low, high = min_max([2, 9, 5])
assert low == 2
assert high == 9


# beat 5 - return a dict. this is the chapter's point
def stats(nums):
    return {"count": len(nums), "sum": sum(nums), "mean": sum(nums) / len(nums)}

assert stats([1, 2, 3]) == {"count": 3, "sum": 6, "mean": 2.0}
assert stats([4]) == {"count": 1, "sum": 4, "mean": 4.0}
assert stats([1, 2]) == {"count": 2, "sum": 3, "mean": 1.5}

print("08 passed")
