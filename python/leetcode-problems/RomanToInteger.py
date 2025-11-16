"""
LeetCode Problem: Roman to Integer (easy)
"""

"""
To solve, first create a dictionary mapping Roman numerals to their respective integer values.
Then, iterare through the string back to front, adding or substract values.
Return the total + the value of the last character.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        
        return total + roman[s[-1]]
