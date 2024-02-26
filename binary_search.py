'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.'''

def bs_helper(nums, target, start, end):
    # If start and end overlap, no solution was found
    if start > end:
        return -1
    # Get middle index
    mid = (start + end) // 2
    # Check if middle value is target
    if nums[mid] == target:
        return mid
    # Depending on middle value, recurse right or left
    if nums[mid] > target:
        return bs_helper(nums, target, start, mid - 1)
    else:
        return bs_helper(nums, target, mid + 1, end)

def binary_search(nums, target):
    return bs_helper(nums, target, 0, len(nums) - 1)


# TESTS

print(binary_search([-1,0,3,5,9,12], 2))
# >>4