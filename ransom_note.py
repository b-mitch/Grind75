'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

from collections import Counter

def can_construct(ransom_note, magazine):
    freq_map = Counter(magazine) # Counter does the below freq map creation but more efficiently
    # freq_map = dict()
    # for char in magazine:
    #     if char in freq_map:
    #         freq_map[char] += 1
    #     else:
    #         freq_map[char] = 1

    # Iterate ransom_note and decrement each characters frequency
    for char in ransom_note:
        # If the character is not in the map or its value is zero, it cannot be used
        if char in freq_map and freq_map[char] > 0:
            freq_map[char] -= 1
        else:
            return False
    return True

# TESTS

print(can_construct('aa','ab'))
# >>False
print(can_construct('aa','aab'))
# >>True