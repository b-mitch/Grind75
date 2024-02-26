'''Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here'''

from collections import Counter

def longest_palindrome(s):
    # Return length if s has one or zero characters
    if len(s) <= 1:
        return len(s)
    # Create character frequency map
    freq_map = Counter(s)
    # Track number of odds and total output
    odds = output = 0
    # Iterate through frequency map values
    for value in freq_map.values():
        # Determine if the value is odd and increment odds counter
        is_odd = value % 2 != 0
        if is_odd:
            odds += 1
        # If not odd or is the first odd, add the full value
        if not is_odd or odds <= 1:
            output += value
        # Otherwise only add the characters even count or zero if value was 1
        else: 
            output += value - 1
    return output



# TESTS

print(longest_palindrome('bananas'))
# >>5