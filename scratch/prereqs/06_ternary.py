# beat 1 - the full form: value_if_true if condition else value_if_false
def sign_word(n):
    raise NotImplementedError


assert sign_word(5) == "positive"
assert sign_word(-3) == "negative"
assert sign_word(0.5) == "positive"


# beat 2 - two conditions, one expression. the second ternary goes in the else slot
def bucket(n):
    raise NotImplementedError


assert bucket(5) == "positive"
assert bucket(-3) == "negative"
assert bucket(0) == "zero"
assert bucket(0.0) == "zero"


# beat 3 - the or default idiom, which the book presents as a shorthand ternary
def display_name(given, fallback):
    raise NotImplementedError


assert display_name("bob", "anon") == "bob"
assert display_name("", "anon") == "anon"
assert display_name(None, "anon") == "anon"
assert display_name(0, "anon") == "anon"
assert display_name("anon", "") == "anon"


# beat 4 - a ternary inside a comprehension. this is the form ARENA actually uses
def clipped(nums, limit):
    raise NotImplementedError


assert clipped([1, 5, 9], 5) == [1, 5, 5]
assert clipped([-2, 7], 0) == [-2, 0]
assert clipped([], 3) == []


# beat 5 - read only. the tuple form, which the book calls un-Pythonic
assert ("no", "yes")[True] == "yes"
assert ("no", "yes")[False] == "no"
assert ("no", "yes")[3 > 1] == "yes"

try:
    (1 / 0, "safe")[True]
    raise AssertionError("both entries are evaluated before the index is applied")
except ZeroDivisionError:
    pass

print("06 passed")
