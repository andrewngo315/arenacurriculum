# beat 1

def sign_word(n):
    return "positive" if n > 0 else "negative"
   

assert sign_word(5) == "positive"
assert sign_word(-3) == "negative"


# beat 2 - the or default idiom
def display_name(given, fallback):
    raise NotImplementedError


assert display_name("bob", "anon") == "bob"
assert display_name("", "anon") == "anon"
assert display_name(None, "anon") == "anon"
assert display_name(0, "anon") == "anon"
assert display_name("anon", "") == "anon"


# beat 3 - read only. the tuple form, which the book calls un-Pythonic
assert ("no", "yes")[True] == "yes"
assert ("no", "yes")[False] == "no"
assert ("no", "yes")[3 > 1] == "yes"

try:
    (1 / 0, "safe")[True]
    raise AssertionError("both entries are evaluated before the index is applied")
except ZeroDivisionError:
    pass

print("06 passed")

