class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make a new array for strings
        newString = [c.lower() for c in s if c.isalnum()]

        return newString == newString[::-1]
