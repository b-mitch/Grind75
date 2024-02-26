'Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'

from collections import Counter

# Simple one liner using Counter to build a freq map and checking for any value >= 2
# def contains_duplicate(nums):
#     return any(val >= 2 for val in Counter(nums).values())

# Faster and less memory used with a set map
# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         else:
#             seen.add(num)
#     return False

# Sort then check adjacent elements is best memory but worst runtime
def contains_duplicate(nums):
    prev = None
    for num in sorted(nums):
        if num == prev:
            return True
        prev = num
    return False

# TESTS

print(contains_duplicate([1,2,3,1]))
# >>True
print(contains_duplicate([1,2,3,4]))
# >>False
