def reverse(nums):

    start_index = 0
    end_index = len(nums) - 1

    while start_index < end_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    return nums


print(reverse([1, 2, 3, 4, 5]))
