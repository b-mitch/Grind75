'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

# Modified two sum with two pointers
def get_two_sums(nums, index):
    # Target is the negative of the current element in our three sum loop
    target = -nums[index]
    output = []
    l = index + 1
    r = len(nums) - 1
    while l < r:
        l_val, r_val = nums[l], nums[r]
        two_sum = l_val + r_val
        # When sum of two is equal to target, we found a triplet that sums to zero
        if two_sum == target:
            output.append([-target, l_val, r_val])
            # Increment/Decrement pointers until on a unique value
            while l < r and nums[l] == l_val:
                l += 1
            while r > l and nums[r] == r_val:
                r -= 1
        elif two_sum < target:
            l += 1
        else:
            r -= 1
    return output

def three_sum(nums):
    output = []
    visited = []
    nums.sort()
    for i, x in enumerate(nums):
        # To avoid duplicates, skip any already visited
        if x in visited:
            continue
        # No positive values will sum to zero
        if x > 0:
            break
        # Add results from two sums helper function
        output += get_two_sums(nums, i)
        visited.append(x)
    return output


# TESTS

print(three_sum([-1,0,1,2,-1,-4]))
# >>[[-1,-1,2],[-1,0,1]]
print('\n')

print(three_sum([-2,0,1,1,2]))
# >>[[-2,0,2],[-2,1,1]]
