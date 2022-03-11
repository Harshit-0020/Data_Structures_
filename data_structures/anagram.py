import time

"""Wrong Method"""
"""
def anagrams_wrong(word1, word2):

    if len(word1) == len(word2) and set(word1) == set(word2):
        return True
    else:
        return False

print(anagrams_wrong('fleet', 'teffl'))
"""


"""Correct Method"""


def anagram_correct(word1, word2):
    if len(word1) == len(word2):
        sorted1 = ''.join(sorted(word1))
        sorted2 = ''.join(sorted(word2))
        if sorted1 == sorted2:
            return True
        else:
            return False


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False


t1 = time.time_ns()
print(anagram_correct('fleet' * (10**4), 'teffl' * (10**4)))
t2 = time.time_ns()
time1 = t2 - t1

t3 = time.time_ns()
print(is_anagram('fleet' * (10**4), 'teffl' * (10**4)))
t4 = time.time_ns()
time2 = t4 - t3

print(f"Time taken by == approach: {time1}")
print(f"Time taken by literal by literal approach: {time2}")


"""
Below announcement overthrown: as results vary, sometimes indexing is faster, sometimes == is faster.
"""
"""
Important announcement: Don't use extreme shortcuts like directly comparing with == instead use literal by literal or index by index in arrays.
"""
