'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

# Less space efficient - O(n)
# def climb_stairs_helper(n, memo):
#     # Base case: if top is passed, return 0
#     if n < 0:
#         return 0
#     # Base case: if top reached, return 1 for one way
#     if n == 0:
#         return 1
#     # Recurse either reducing n by one or two to represent stairs taken using memoization
#     if n - 1 not in memo:
#         memo[n - 1] = climb_stairs_helper(n - 1, memo)
#     ways_1 = memo[n - 1]
#     if n - 2 not in memo:
#         memo[n - 2] = climb_stairs_helper(n - 2, memo)
#     ways_2 = memo[n - 2]

#     return ways_1 + ways_2

# def climb_stairs(n):
#     # Initialize empty map for memoization
#     memo = dict()
#     return climb_stairs_helper(n, memo)

# More space efficient - O(1)
def climb_stairs(n):
    # If only one or two stairs, that's the number of possible ways
    if n <= 2:
        return n
    # Set a previous and current ways tracker
    prev, curr = 1, 2
    # Each solution for n steps is the sum of the solutions for n - 1 and n - 2 steps
    # So iterate n steps starting at 3 and incrementing the total based on the previous two
    for _ in range(3, n + 1):
        prev, curr = curr, curr + prev

    return curr


# TESTS

print(climb_stairs(2))
# >>2
print(climb_stairs(38))
# >>3