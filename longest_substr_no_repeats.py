'Given a string s, find the length of the longest substring without repeating characters.'

# Use sliding window to track longest substring with no repeats - O(n) time & space
def length_of_longest_substring(s):
    if len(s) == 0:
        return 0
    l = r = 0
    in_window = dict()
    longest = 0
    while r < len(s):
        char = s[r]
        # Check if character is a repeat
        if char not in in_window:
            # If not, add to frequency map
            in_window[char] = r
            # Calculate length and replace output if longer
            longest = r - l + 1 if r - l + 1 > longest else longest
            # Increment right pointer one
            r += 1
        else:
            # If character is a repeat, shift left pointer over if repeat is in the current window
            if in_window[char] >= l:
                l = in_window[char] + 1
            # Remove that character from the current window character map
            del in_window[char]
    return longest
        

# TESTS

print(length_of_longest_substring('abba'))
# >>3 (abc)
print(length_of_longest_substring('pwwkew'))
# >>3 (wke)