import ast
import inspect
from pickle import TRUE
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
def square(a):
    return a ** 2

def squares(nums):
    return list(map(square, nums))
    

print(squares([1, 2, 3]))
assert squares([1, 2, 3]) == [1, 4, 9]
assert squares([]) == []


# beat 2 - filter
def even(a):
        if a % 2 == 0:
            return True
        if a == 0:
            return True  
def evens(nums):
    return list(filter(even, nums))

print(evens([0, 1, 2]))
assert evens([1, 2, 3, 4]) == [2, 4]
assert evens([1, 3]) == []
assert evens([0, 1, 2]) == [0, 2]


# beat 3 - reduce, and its initial-value argument
def multiplication(a, b):
    return a * b 

def product(nums):
    return reduce(multiplication, nums, 1)
    

assert product([1, 2, 3, 4]) == 24
assert product([5]) == 5
assert product([]) == 1


# beat 4 - max with a key
def longest(words):
        return max(words, key=len)

assert longest(["hi", "hello", "hey"]) == "hello"
assert longest(["a"]) == "a"

assert _calls(squares, "map"), "squares must use map"
assert _calls(evens, "filter"), "evens must use filter"
assert _calls(product, "reduce"), "product must use reduce"

print("04 passed")
