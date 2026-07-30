class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        lenS = len(s)
        
        # loop through the s
            # compare front and back
        for i in range(lenS//2):
            if s[i] != s[lenS - (i + 1)]:
                return False
        return True
        