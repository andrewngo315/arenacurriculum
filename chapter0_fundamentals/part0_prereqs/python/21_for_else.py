import ast
import inspect
import textwrap


# checker - reads your source to confirm each one really uses for/else
def _uses_for_else(fn):
    tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
    return any(isinstance(n, ast.For) and n.orelse for n in ast.walk(tree))


# beat 1 - the one that needs a guard before the loop
def is_prime(n):
    raise NotImplementedError


assert is_prime(2) is True
assert is_prime(7) is True
assert is_prime(9) is False
assert is_prime(1) is False
assert is_prime(4) is False
assert is_prime(25) is False
assert is_prime(49) is False
assert is_prime(97) is True
assert is_prime(0) is False
assert is_prime(-7) is False
assert _uses_for_else(is_prime), "is_prime must use for/else"


# beat 2 - found, or fell off the end
def first_negative(nums):
    raise NotImplementedError


assert first_negative([3, -1, 4, -5]) == -1
assert first_negative([1, 2]) is None
assert first_negative([]) is None
assert _uses_for_else(first_negative), "first_negative must use for/else"


# beat 3 - no counterexample found
def all_shorter_than(words, limit):
    raise NotImplementedError


assert all_shorter_than(["hi", "yo"], 5) is True
assert all_shorter_than(["hi", "hello"], 5) is False
assert all_shorter_than([], 5) is True
assert _uses_for_else(all_shorter_than), "all_shorter_than must use for/else"


# beat 4 - nested loops, first pair in index order
def find_pair_summing_to(nums, target):
    raise NotImplementedError


assert find_pair_summing_to([1, 2, 3, 4], 7) == (3, 4)
assert find_pair_summing_to([1, 2], 100) is None
assert find_pair_summing_to([3, 5], 6) is None
assert find_pair_summing_to([1, 2, 3, 4], 5) == (1, 4)
assert _uses_for_else(find_pair_summing_to), "find_pair_summing_to must use for/else"

print("21 passed")
