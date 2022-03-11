integer = 12340
rev_num = 0

while integer > 0:
    last_digit = integer % 10
    rev_num = rev_num * 10 + last_digit
    integer = integer // 10

""" This is also order of N -  O(N) time complexity algorithm."""

print(rev_num)
