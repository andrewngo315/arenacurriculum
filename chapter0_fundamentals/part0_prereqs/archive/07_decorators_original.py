def shout(text):
    return text.upper()
loud = shout("hi")


def apply_twice(f, x): # this function was written by me
    i = f(x)
    j = f(i)
    return j

def add_one(n):
    return n + 1

assert apply_twice(add_one, 5) == 7
print("passed")

# beat 3
def make_multiplier(n):
    def f(x):
        return n * x
    return f

double = make_multiplier(2)
triple = make_multiplier(3)

assert double(5) == 10
assert triple(5) == 15
assert double(triple(2)) == 12
print("passed")
    
print(double)
print(triple)
print(double is triple)

# beat 4 + 5
def make_loud(x):
    def func(text):
        return x(text) + "!!!"
    return func

shout_loud = make_loud(shout)

assert shout_loud("hi") == "HI!!!"
assert shout("hi") == "HI"
print("passed")

def whisper(text):
    return text.lower()

quiet_loud = make_loud(whisper)
assert quiet_loud("HI") == "hi!!!"
print("passed for real")

@make_loud
def greet(text):
    return "hello " + text

assert greet("bob") == "hello bob!!!"
print("beat 5 passed")

# beat 6 - a decorator that takes arguments needs one more layer of nesting
@make_loud()
def greet2(text):
    return "hi " + text