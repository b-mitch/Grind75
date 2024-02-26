'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

from collections import Counter

# O(n) time, O(n) space; n = distinct elements
# def majority_element(nums):
#     freq_map = Counter(nums)
#     majority = len(nums) / 2

#     return [key for key, value in freq_map.items() if value >= majority][0]

# O(n) time, O(1) space
# Boyer-Moore Majority Vote Algorithm
def majority_element(nums):
    majority = 0
    count = 0
    # Iterate nums and track the current majority_element and its count, 
    # switching to the current element when its count reaches to zero
    for element in nums:
        if count == 0:
            majority = element
        if element != majority:
            count -= 1
        else:
            count += 1
    return majority
    

# TESTS

print(majority_element([2,2,1,1,1,2,2]))
# >> 2
