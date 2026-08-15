# beat 1 - a generator yields, it does not return a list
from operator import index
from tkinter import N


def countdown(n):
    while n > 0:
        yield n
        n = n - 1
    


assert list(countdown(3)) == [3, 2, 1]
assert list(countdown(0)) == []
assert type(countdown(3)).__name__ == "generator"
assert list(countdown(5)) == [5, 4, 3, 2, 1]

# beat 2 - pull k items and stop
def take(iterable, k):
    l = []
    for i in iterable:
        if len(l) < k:
            l.append(i)
        if len(l) == k:
            break
    return l


assert take(countdown(10), 3) == [10, 9, 8]
assert take([1, 2], 5) == [1, 2]
assert take([1, 2, 3], 0) == []

# checker - nothing to write below this line
def _limited():
    for n in [10, 9, 8, 7, 6]:
        yield n
    raise AssertionError("take kept pulling after k items")


assert take(_limited(), 3) == [10, 9, 8]


# beat 3 - an infinite generator, safe only because take stops pulling
def fib():
    fibs = [1, 1]
    yield fibs[0]
    yield fibs[1]
    while True:
        fibs.append(fibs[-1] + fibs[-2])
        yield fibs[-1]


assert take(fib(), 8) == [1, 1, 2, 3, 5, 8, 13, 21]
assert type(fib()).__name__ == "generator"

print("03 passed")
