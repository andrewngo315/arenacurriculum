# beat 1 - *args collects positional arguments into a tuple
def total(*args):
    return sum(args)


assert total(1, 2, 3) == 6
assert total() == 0
assert total(5) == 5

# beat 2 - the same star at the call site, unpacking a list
nums = [1, 2, 3]
assert total(*nums) == 6


# beat 3 - **kwargs collects keyword arguments into a dict
def describe(**kwargs):
    parts = []
    for key in sorted(kwargs):
        parts.append(f'{key}={kwargs[key]}')
    return ", ".join(parts)

assert describe(a=1, b=2) == "a=1, b=2"
assert describe(b=2, a=1) == "a=1, b=2"
assert describe() == ""


# beat 4 - forward both, untouched, to any function
def call_with(f, *args, **kwargs):
    return f(*args, **kwargs)


def greet(name, greeting="hello", punctuation="!"):
    return greeting + " " + name + punctuation


assert call_with(greet, "bob") == "hello bob!"
assert call_with(greet, "bob", greeting="hi") == "hi bob!"
assert call_with(greet, "bob", "yo", punctuation="?") == "yo bob?"

# beat 5 - double star at the call site, unpacking a dict
opts = {"greeting": "hey", "punctuation": "."}
assert greet("ann", **opts) == "hey ann."
assert call_with(max, 3, 9, 4) == 9
assert call_with(sorted, [3, 1, 2], reverse=True) == [3, 2, 1]

# beat 6 - retention check, write from memory without scrolling up
def twice(f, *args, **kwargs):
    return (f(*args, **kwargs), f(*args, **kwargs))
    

assert twice(greet, "bob") == ("hello bob!", "hello bob!")
assert twice(greet, "bob", greeting="hi") == ("hi bob!", "hi bob!")
assert twice(max, 3, 9, 4) == (9, 9)
assert twice(sorted, [3, 1, 2], reverse=True) == ([3, 2, 1], [3, 2, 1])

print("01 passed")
