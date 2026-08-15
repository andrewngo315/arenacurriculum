from collections import defaultdict, Counter, namedtuple, deque
from enum import Enum


# beat 1 - defaultdict(list)
def group_by_first_letter(words):
    raise NotImplementedError


assert group_by_first_letter(["ant", "bee", "ape"]) == {"a": ["ant", "ape"], "b": ["bee"]}
assert group_by_first_letter([]) == {}


# beat 2 - Counter.most_common
def top_words(text, n):
    raise NotImplementedError


assert top_words("a b a c a b", 2) == [("a", 3), ("b", 2)]
assert top_words("x y", 1) == [("x", 1)]


# beat 3 - build the namedtuple type
Card = None
if Card is None:
    raise NotImplementedError


# beat 4 - and construct one
def make_card(rank, suit):
    raise NotImplementedError


c = make_card("A", "spades")
assert c.rank == "A"
assert c.suit == "spades"
assert c == ("A", "spades")
assert Card._fields == ("rank", "suit")

d = make_card(7, "hearts")
assert d.rank == 7
assert d.suit == "hearts"
assert d == (7, "hearts")
assert isinstance(d, Card)


# beat 5 - deque with maxlen
def last_n(items, n):
    raise NotImplementedError


r = last_n([1, 2, 3, 4, 5], 3)
assert isinstance(r, deque)
assert r.maxlen == 3
assert list(r) == [3, 4, 5]
r.appendleft(0)
assert list(r) == [0, 3, 4]
assert list(last_n([1], 3)) == [1]
assert list(last_n([], 2)) == []


# given - an Enum, already written
class Suit(Enum):
    spades = 1
    hearts = 2


assert Suit.spades.value == 1
assert Suit(2) is Suit.hearts
assert Suit["spades"] is Suit.spades


# beat 6 - look a member up by its value
def suit_name(value):
    raise NotImplementedError


assert suit_name(1) == "spades"
assert suit_name(2) == "hearts"

print("12 passed")
