'''You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.'''

# Modified binary search
def first_bad_helper(low, high):
    # Final recursive call will provide first bad version
    if low == high - 1:
        return low if is_bad_version(low) else high
    
    mid = (low + high) // 2
    # Continue recursing right or left depending whether or not mid is bad
    if is_bad_version(mid):
        return first_bad_helper(low, mid)
    return first_bad_helper(mid, high)

def first_bad_version(n):
    return first_bad_helper(0, n)

# TESTS
# Helper function for testing
bad_version = 4
def is_bad_version(version):
    if version >= bad_version:
        return True
    return False
print(first_bad_version(5))
# >>4