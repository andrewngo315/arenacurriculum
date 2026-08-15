import functools


def shout(text):
    return text.upper()


# beat 1 - a function is an object. bind the function itself, do not call it
alias = shout

assert alias("hi") == "HI"
assert alias is shout
assert callable(alias)


# beat 2 - a function taken as an argument
def apply_twice(f, x):
    a = f(x)
    b = f(a)
    return b


def add_one(n):
    return n + 1


assert apply_twice(add_one, 5) == 7
assert apply_twice(str.upper, "a") == "A"
assert apply_twice(lambda n: n * 2, 3) == 12


# beat 3 - a function returned from a function, closing over n
def make_multiplier(n):
    def inner(x):
        return n * x
    return inner


double = make_multiplier(2)
triple = make_multiplier(3)

assert double(5) == 10
assert triple(5) == 15
assert double(triple(2)) == 12
assert (double is triple) is False


# beat 4 - a decorator built by hand: takes a function, returns a new one
def make_loud(f):
    def inner(x):
        return f(x) + "!!!"
    return inner


shout_loud = make_loud(shout)

assert shout_loud("hi") == "HI!!!"
assert shout("hi") == "HI"


def whisper(text):
    return text.lower()


assert make_loud(whisper)("HI") == "hi!!!"


# beat 5 - read only. the @ line is only sugar for greet = make_loud(greet)
@make_loud
def greet(name):
    return "hello " + name


assert greet("bob") == "hello bob!!!"


# beat 6 - a wrapper that decorates any signature, and keeps the name it wrapped
def loud(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs) + "!!!"
    return inner

@loud
def greet2(name, greeting="hello"):
    return greeting + " " + name


assert greet2("bob") == "hello bob!!!"
assert greet2("bob", greeting="hi") == "hi bob!!!"
assert greet2("bob", "yo") == "yo bob!!!"
assert greet2.__name__ == "greet2"
assert greet.__name__ != "greet"


# beat 7 - @thing() takes arguments, so it needs one more layer than @thing
def repeat(n):
    def decorator(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            return f(*args, **kwargs) * n
        return inner
    return decorator

        


@repeat(3)
def hi():
    return "hi"


@repeat(1)
def yo(name):
    return "yo " + name


assert hi() == "hihihi"
assert yo("bob") == "yo bob"
assert hi.__name__ == "hi"

print("07 passed")
