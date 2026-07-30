class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            count.setdefault(c, 1)

        for c in t:
            if c not in count or count[c] < 1:
                return False
            else:
                count[c] -= 1
        return True


