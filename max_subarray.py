'Given an integer array nums, find the subarray with the largest sum, and return its sum.'
'A subarray is a contiguous non-empty sequence of elements within an array.'

import math
# 0(n) time and space with sliding window
def max_subarray(nums):
    # Account for empty lists
    if len(nums) == 0:
        return 0
    # Set left and right pointers for sliding window
    l = r = 0
    # Set sum tracking variables
    max_sum = -math.inf
    curr_sum = nums[0]
    while r < len(nums):
        # Check if current sum should become the max
        if curr_sum > max_sum:
            max_sum = curr_sum
        # If current sum is below 0, throw out that subarray and start anew at next index
        if curr_sum < 0:
            r = r + 1
            l = r
            if r < len(nums):
                curr_sum = nums[r]
        # If current sum is 0 or greater, increment right pointer and update current sum
        elif curr_sum >= 0:
            r += 1
            if r < len(nums):
                curr_sum += nums[r]
    return max_sum

# TESTS

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
# >>6

print(max_subarray([5,4,-1,7,8]))
# >>23

print(max_subarray([-1,-2]))
# >>1