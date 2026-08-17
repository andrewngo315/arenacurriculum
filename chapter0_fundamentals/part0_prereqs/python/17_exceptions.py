# given - your own exception type
class TooSmallError(Exception):
    pass


# beat 1 - try / except ZeroDivisionError, not an if
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


assert safe_div(6, 3) == 2
assert safe_div(1, 0) is None
assert safe_div(7, 2) == 3.5


# beat 2 - except ValueError
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return 0


assert parse_int("42") == 42
assert parse_int("nope") == 0
assert parse_int("") == 0
assert parse_int("-5") == -5
assert parse_int(" 42 ") == 42


log = []


# beat 3 - raise your own, and finally runs either way
def guarded(n):
    try: 
        if n < 5:
            raise TooSmallError(f"{n} is too small")
        return n    
    finally:
            log.append("done")
    
            
    
assert guarded(10) == 10
assert log == ["done"]

try:
    guarded(1)
except TooSmallError as e:
    assert str(e) == "1 is too small"
else:
    raise AssertionError("guarded(1) should have raised TooSmallError")

assert log == ["done", "done"]

assert guarded(5) == 5

try:
    guarded(4)
except TooSmallError as e:
    assert str(e) == "4 is too small"
else:
    raise AssertionError("guarded(4) should have raised TooSmallError")

try:
    guarded("x")
except TypeError:
    pass

assert log == ["done"] * 5


# beat 4 - the one place a broad except Exception is right
def first_working(funcs):
    for f in funcs:
        try:
            return f()
        except Exception:
            continue
        return None


def boom():
    raise ValueError("nope")


def fine():
    return "ok"


assert first_working([boom, fine]) == "ok"
assert first_working([boom, boom]) is None


def div_zero():
    return 1 / 0


# beat 5 - two separate except blocks
def classify(f):
    try:
        return f()
    except ZeroDivisionError:
        return "zero"
    except ValueError:
        return "value"


assert classify(div_zero) == "zero"
assert classify(boom) == "value"
assert classify(fine) == "ok"

print("17 passed")
