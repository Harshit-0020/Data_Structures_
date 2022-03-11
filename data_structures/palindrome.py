def is_palindrome(string):
    return string == string[::-1]


def reverse_string(string):

    string = list(string)
    start_index = 0
    end_index = len(string) - 1
    while start_index < end_index:
        string[start_index], string[end_index] = string[end_index], string[start_index]
        start_index += 1
        end_index -= 1
    return ''.join(string)


# Implementation using array reversal:

# This has O(n): linear running time complexity as far as number of characters in the string is considered.
def palindrome(string):
    return string == reverse_string(string)


print(palindrome('car'))
