'Given two binary strings a and b, return their sum as a binary string.'

def prepend_zeros(s, x):
    zeros = ''
    for _ in range(x - len(s)):
        zeros += '0'
    s = zeros + s
    return s

def add_binary(a, b):
    # Add zeros to front of short string with helper function
    if len(a) != len(b):
        if len(a) < len(b):
            a = prepend_zeros(a, len(b)) 
        else:
            b = prepend_zeros(b, len(a))
    remainder = 0
    output = ''
    # Iterate both strings in reverse, adding current elements and remainder
    for i in range(len(a) - 1, -1, -1):
        temp_sum = int(a[i]) + int(b[i]) + remainder
        # Make sure you carry over 1 if the sum is 2 or more
        if temp_sum >= 2:
            remainder = 1
        else:
            remainder = 0
        # Reassign sum appropriately based on binary addition rules
        if temp_sum == 2:
            temp_sum = 0
        elif temp_sum == 3:
            temp_sum = 1
        output = str(temp_sum) + output
    if remainder:
        output = '1' + output
    return output
    

# TESTS

print(add_binary('11', '1'))
# >> '100'
print(add_binary('1010', '1011'))
# >> '10101'
print(add_binary('1111', '1111'))
# >> '11110'
