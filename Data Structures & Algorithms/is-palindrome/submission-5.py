class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make a new array for strings
        newString = [c.lower() for c in s if c.isalnum()]

        for i in range(len(newString)//2):
            if newString[i] != newString[len(newString) - (i+1)]:
                return False
        return True
