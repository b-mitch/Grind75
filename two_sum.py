'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

# Slightly optimized solution with small chatgpt hint

# My answer - 0(n log n) because of the sort
def two_sum(nums, target):
    indices = []
    for i, digit in enumerate(nums):
        indices.append((digit, i))
    # Chatgpt HINT to sort list of tuples based on first tuple value
    indices.sort(key=lambda x: x[0])
    big = len(indices) - 1
    small = big - 1
    # Use two pointers to find target sum
    while 0 <= small < len(indices) and 0 <= big < len(indices):
        sum = indices[small][0] + indices[big][0]
        if sum == target:
            return [indices[small][1], indices[big][1]]
        if sum < target:
            big += 1
        elif sum > target:
            big -= 1
            small -= 1
    return []

# O(n) without sort
def two_sum_opt(nums, target):
    diffs = dict()
    # Iterate nums
    for i, n in enumerate(nums):
        # If the number is in differences map, return its index and the mapped index
        if n in diffs:
            return [diffs[n], i]
        # Else, map the difference of the target the number to its index
        diffs[target - n] = i

# TESTS

print(two_sum([3,2,4], 6))
print(two_sum_opt([3,2,4], 6))