class Solution:
    def isPalindrome(self, s: str) -> bool:
        # have 2 pointers, one beginning, one end
        # convert string to lower case
        newString = []
        for c in s:
            if c.isalnum():
                newString.append(c.lower())

        l = 0
        r = len(newString) - 1

        while l < r:
            if newString[l] != newString[r]:
                return False

            l += 1
            r -= 1
        return True