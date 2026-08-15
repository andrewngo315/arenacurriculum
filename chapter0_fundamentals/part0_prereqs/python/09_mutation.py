# beat 1 - the mutable default trap. write the obvious body first and watch it fail
def append_to(item, target=[]):
    raise NotImplementedError


assert append_to(1) == [1]
assert append_to(2) == [2]
assert append_to(3, [0]) == [0, 3]


# beat 2 - returns a new list, leaves the caller's alone
def doubled(nums):
    raise NotImplementedError


original = [1, 2, 3]
assert doubled(original) == [2, 4, 6]
assert original == [1, 2, 3]


# beat 3 - returns None, edits the caller's list
def double_in_place(nums):
    raise NotImplementedError


original = [1, 2, 3]
assert double_in_place(original) is None
assert original == [2, 4, 6]


# beat 4 - read only. identity vs equality
a = [1, 2, 3]
b = a
c = list(a)
a.append(4)

assert b == [1, 2, 3, 4]
assert c == [1, 2, 3]
assert (a is b) is True
assert (a is c) is False

print("09 passed")
