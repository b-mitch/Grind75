'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''

# Helper function to remove spaces and special characters
def convert_to_alphanumeric(s):
    output = ''
    for char in s:
        if char.isdigit() or char.isalpha():
            output += char
    return output.lower()

def is_palindrome(s):
    if len(s) <= 1:
        return True
    alphanum_s = convert_to_alphanumeric(s)
    # Set start and end pointers
    start, end = 0, len(alphanum_s) - 1
    # Iterate string from outside in
    while start <= end:
        # Not a palindrome if the values at oppposite pointers don't match
        if alphanum_s[start] != alphanum_s[end]:
            return False
        start += 1
        end -= 1
    return True

# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     start = 0
#     end = len(s) - 1
#     while start <= end:
#         if (s[start].isdigit() or s[start].isalpha()) and (s[end].isdigit() or s[end].isalpha()):
#             if s[start].lower() != s[end].lower():
#                 return False
#             else:
#                 start += 1
#                 end -= 1
#         else:
#             if not s[start].isdigit() and not s[start].isalpha():
#                 start += 1
#             if not s[end].isdigit() and not s[end].isalpha():
#                 end -= 1
#     return True

# TESTS

print(is_palindrome("A man, a plan, a canal: Panama"))
# >>True
print(is_palindrome("raceacar"))
# >>False