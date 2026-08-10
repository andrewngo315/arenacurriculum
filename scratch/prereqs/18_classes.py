# beat 1 - __init__, methods, __repr__, and a class attribute that counts instances
class Account:
    count = None

    def __init__(self, owner, balance):
        raise NotImplementedError

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError


# beat 2 - inheritance and super()
class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        raise NotImplementedError

    def add_interest(self):
        raise NotImplementedError


if Account.count is None:
    raise NotImplementedError
assert Account.count == 0

a = Account("bob", 100)
assert a.owner == "bob"
assert a.balance == 100

a.deposit(50)
assert a.balance == 150

a.withdraw(30)
assert a.balance == 120

try:
    a.withdraw(1000)
except ValueError as e:
    assert str(e) == "insufficient funds"
else:
    raise AssertionError("overdraw should have raised ValueError")

assert a.balance == 120
assert repr(a) == "Account(bob, 120)"

b = Account("ann", 0)
assert b.balance == 0
assert a.balance == 120

assert Account.count == 2

s = SavingsAccount("cat", 200, 0.1)
assert Account.count == 3
assert isinstance(s, Account)
assert s.balance == 200

s.deposit(100)
assert s.balance == 300

s.add_interest()
assert s.balance == 330
assert repr(s) == "SavingsAccount(cat, 330.0)"


# beat 3 - the mutable class-variable trap
class Tally:
    def __init__(self):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError


t1 = Tally()
t2 = Tally()
t1.add("a")
assert t1.items == ["a"]
assert t2.items == []


# beat 4 - __getitem__, the protocol PyTorch's Dataset uses
class Deck:
    def __init__(self, cards):
        raise NotImplementedError

    def __getitem__(self, i):
        raise NotImplementedError


d = Deck(["ace", "king", "queen"])
assert d[0] == "ace"
assert d[-1] == "queen"

print("18 passed")
