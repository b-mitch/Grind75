'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.'''

# Optimized solution without hints

# O(n)
def valid_parentheses(s):
    # Init a stack to track which paren type must be closed first
    stack = []
    # Init a map to track each parens state
    states = {'round': 0, 'square': 0, 'curly': 0}
    left = '([{'
    right = ')]}'
    types = ['round','square','curly']
    current_type = None
    for char in s:
        # If a left paren, increment its mapped state and append the paren type to the stack
        if char in left:
            current_type = types[left.index(char)]
            stack.append(current_type)
            states[current_type] += 1
        # If a right paren, make sure it's closing the most recent paren type 
        # and decrement its mapped state
        if char in right:
            current_type = types[right.index(char)]
            if len(stack) == 0 or stack[-1] != current_type:
                return False
            else:
                stack.pop()
            states[current_type] -= 1
        # If any states are below 0, there are more right than left parens for that type, 
        # which is not valid
        if states[current_type] < 0:
            return False
    # Return whether all parens have been closed
    return all(value == 0 for value in states.values())

# TESTS

print(valid_parentheses("([])"))
print(valid_parentheses("([)]"))