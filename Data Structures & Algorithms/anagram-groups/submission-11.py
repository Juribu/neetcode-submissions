class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = set()

        for s in range(len(strs)):
            if s in visited:
                continue

            group = [strs[s]]
            visited.add(s)

            for t in range(s+1, len(strs)):
                if t not in visited and self.isAnagram(strs[s], strs[t]):
                    group.append(strs[t])
                    visited.add(t)

            result.append(group)

        return result

    def isAnagram(self, a: str, b: str) -> bool:
        return sorted(a) == sorted(b)