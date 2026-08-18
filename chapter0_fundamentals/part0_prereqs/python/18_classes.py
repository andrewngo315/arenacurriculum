# beat 1 - __init__, methods, __repr__, and a class attribute that counts instances
class Account:
    count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Account.count = Account.count + 1

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            self.balance = self.balance + amount
            raise ValueError("insufficient funds")
        
    def __repr__(self):
        return f"{type(self).__name__}({self.owner}, {self.balance})"


# beat 2 - inheritance and super()
class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate
        

    def add_interest(self):
        self.balance = self.balance * (1 + self.rate)
    



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
        self.items = []

    def add(self, item):
        self.items.append(item)


t1 = Tally()
t2 = Tally()
t1.add("a")
assert t1.items == ["a"]
assert t2.items == []


# beat 4 - __getitem__, the protocol PyTorch's Dataset uses
class Deck:
    def __init__(self, cards):
        self.cards = cards 

    def __getitem__(self, i):
        return self.cards[i]


d = Deck(["ace", "king", "queen"])
assert d[0] == "ace"
assert d[-1] == "queen"

print("18 passed")
