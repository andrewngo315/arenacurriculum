# beat 1 - enumerate takes a start argument
def numbered(items):
    raise NotImplementedError


assert numbered(["a", "b"]) == ["1. a", "2. b"]
assert numbered([]) == []


# beat 2 - first index wins a tie
def index_of_max(nums):
    raise NotImplementedError


assert index_of_max([3, 9, 4]) == 1
assert index_of_max([5]) == 0
assert index_of_max([1, 9, 9]) == 1


# beat 3 - every index where the target appears
def positions(items, target):
    raise NotImplementedError


assert positions(["a", "b", "a"], "a") == [0, 2]
assert positions(["a"], "z") == []

print("13 passed")
