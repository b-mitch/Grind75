'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

def is_anagram(s, t):
    # They cannot be anagrams if they're different lengths
    if len(s) != len(t):
        return False
    # Create dictionary to track character counts
    freq = dict()
    for i in range(len(s)):
        val_s = s[i]
        val_t = t[i]
        # Increment character count if in list s
        if val_s in freq:
            freq[val_s] += 1
        else:
            freq[val_s] = 1
        # Decrement character count if in list t
        if val_t in freq:
            freq[val_t] -= 1
        else:
            freq[val_t] = -1
    # If they're anagrams then they have the same count of each character so all should be zero
    return all(val == 0 for val in freq.values())

# TESTS

print(is_anagram('anagram', 'nagaram'))
# >>True

print(is_anagram('ac', 'bb'))
# >>False