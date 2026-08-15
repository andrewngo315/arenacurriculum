# beat 1 - average. step with n, inspect with p, continue with c
def average(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
    return total / len(nums)


assert average([2, 4, 6]) == 4
assert average([10]) == 10
assert average([1, 2, 3, 4]) == 2.5


# beat 2 - count_vowels
def count_vowels(word):
    count = 0
    for letter in word:
        if letter.lower() in "aeiou":
            count = count + 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("rhythm") == 0
assert count_vowels("AEIOU") == 5


# beat 3 - last_word
def last_word(sentence):
    words = sentence.split()
    if len(words) > 0:
        return words[-1]
        
assert last_word("the cat sat") == "sat"
assert last_word("hello") == "hello"
assert last_word("") is None

print("02 passed")
