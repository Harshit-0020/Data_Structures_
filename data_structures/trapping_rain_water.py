"""
Trapping rain water problem:
We need to find the amount of water trapped inside the bars defined by the array.
"""


"""
Method 1:-

We use the formula --

min(max_left, max-right) - height_of_current bar.

(It takes O(N^2) running time complexity and therefore not used.)
"""


def total_water_trapped_quad_comp(bars):                                    # O(N^2)

    total_water_trapped = 0

    if len(bars) < 3:
        return 0

    for i in range(len(bars)):                                              # O(N)

        if (i == 0) or (i == len(bars) - 1):
            water_trapped_by_current_bar = 0
        else:
            max_left = max(bars[:i])                                        # O(N^2)
            max_right = max(bars[i+1:])                                     # O(N^2)
            current_bar = bars[i]

            min_of_max = min(max_left, max_right)

            if current_bar > min_of_max:
                water_trapped_by_current_bar = 0
            else:
                water_trapped_by_current_bar = min_of_max - current_bar

        total_water_trapped += water_trapped_by_current_bar

    return total_water_trapped


"""
Method 2:-
We use dynamic programming to pre-compute the maximum left/right bars.
(Here we pre-compute the max values(linear running time complexity) 
and another linear for going through to get water trapped by each bar.)
"""


def total_water_trapped_linear(bars):       # O(N)

    if len(bars) < 3:
        return 0

    max_left_array = []
    current_max_left = 0

    for i in range(len(bars)):
        max_left_array.append(current_max_left)    # O(N)
        if bars[i] > current_max_left:
            current_max_left = bars[i]

    max_right_array = []
    current_max_right = 0
    for i in range(len(bars)-1, -1, -1):   # Going from L to R in the array, then reverse the max_right_array in the end
        max_right_array.append(current_max_right)           # O(N)
        if bars[i] > current_max_right:
            current_max_right = bars[i]

    max_right_array.reverse()  # In place reversal.

    total_water_trapped = 0

    for i in range(len(bars)):
        water_trapped = min(max_left_array[i], max_right_array[i]) - bars[i]     # O(N)
        if water_trapped < 0:
            total_water_trapped += 0
        else:
            total_water_trapped += water_trapped

    return total_water_trapped


if __name__ == '__main__':
    bars = [1, 0, 2, 1, 3, 1, 2, 0, 3]
    print(f"Total Water trapped linear time complexity: {total_water_trapped_linear(bars)}")
    print(f"Total water trapped quadratic time complexity: {total_water_trapped_quad_comp(bars)}")
