def shout(word):
    return word.upper() + "!"


def shout_all(words):
    out = []
    for w in words:
        out.append(shout(w))
    return out


assert shout_all(["hi", "there"]) == ["HI!", "THERE!"]
assert shout_all(["a", 2, "c"]) == ["A!", "2!", "C!"]
assert shout_all([]) == [""]
assert shout("no") == "NO"

print("traceback_check passed")
