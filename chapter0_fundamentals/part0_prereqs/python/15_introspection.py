# given - two classes to inspect
class Robot:
    wheels = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "beep"

    def _secret(self):
        return "shh"


class Drone:
    kind = "quad"

    def __init__(self):
        self.id = 7
        self.alt = 100


# beat 1 - dir, callable, getattr
def public_methods(obj):
    out = []
    for name in dir(obj):
        if not name.startswith("_") and callable(getattr(obj, name)):
            out.append(name)
    return out



assert public_methods(Robot("r2")) == ["speak"]
assert public_methods([1, 2]) == sorted(m for m in dir([]) if not m.startswith("_"))


# beat 2 - vars. instance attributes only
def attributes(obj):
    return vars(obj) # returns the dictionary


assert attributes(Robot("r2")) == {"name": "r2"}
assert attributes(Drone()) == {"id": 7, "alt": 100}


# beat 3 - the type's name as a string
def describe(obj):
    return type(obj).__name__


assert describe(5) == "int"
assert describe("hi") == "str"
assert describe(Robot("r2")) == "Robot"
assert describe([1]) == "list"
assert describe(3.5) == "float"
assert describe({}) == "dict"
assert describe(None) == "NoneType"
assert describe(Drone()) == "Drone"


# beat 4 - id, or equivalently is
def same_object(a, b):
    return id(a) == id(b) # return a is b also works


x = [1, 2]
y = x
z = [1, 2]
assert same_object(x, y) is True
assert same_object(x, z) is False
assert x == z

print("15 passed")
