import ast
import inspect
import textwrap
from functools import reduce


# checker - reads your source to confirm you used the real function
def _calls(fn, name):
    tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
    return any(
        isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name
        for n in ast.walk(tree)
    )


# beat 1 - map
def squares(nums):
    raise NotImplementedError


assert squares([1, 2, 3]) == [1, 4, 9]
assert squares([]) == []


# beat 2 - filter
def evens(nums):
    raise NotImplementedError


assert evens([1, 2, 3, 4]) == [2, 4]
assert evens([1, 3]) == []


# beat 3 - reduce, and its initial-value argument
def product(nums):
    raise NotImplementedError


assert product([1, 2, 3, 4]) == 24
assert product([5]) == 5
assert product([]) == 1


# beat 4 - max with a key
def longest(words):
    raise NotImplementedError


assert longest(["hi", "hello", "hey"]) == "hello"
assert longest(["a"]) == "a"

assert _calls(squares, "map"), "squares must use map"
assert _calls(evens, "filter"), "evens must use filter"
assert _calls(product, "reduce"), "product must use reduce"

print("04 passed")
