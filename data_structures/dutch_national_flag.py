# Dutch National Flag Problem.

# Here the middle value is called "pivot value" -- in this case value 1.

T = [0, 1, 2, 1, 2, 0, 1, 1, 0]

"""
We initialise i and j as 0s while k is the last index.
 We take three indices i, j, k where i tracks the first cluster, j tracks the current item, k tracks the last cluster.
 That means i tracks 0s, j tracks current number in the list, k tracks 2s.
 
 In every iteration we compare the jth item with the pivot item.
 
 If the current value is greater than pivot value, then we swap numbers at j and k and reduce k by 1.
 If the current value is smaller than the pivot value, then we swap nums at i and j and increment both i and j
 
 This continues until j > k.
"""


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


i = 0
j = 0
k = len(T) - 1
mid_value = 1

while k > j:
    if T[j] < mid_value:
        swap(T, i, j)
        i += 1
        j += 1

    elif T[j] > mid_value:
        swap(T, j, k)
        k -= 1
    else:
        j += 1  # If the value is same as mid_value then we leave it untouched and move forward.


print(T)
