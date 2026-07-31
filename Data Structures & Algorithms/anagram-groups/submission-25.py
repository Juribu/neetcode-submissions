class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            result[tuple(count)].append(s)

        return list(result.values())

        # make a default dictionary/hashmap of lists
        # for each string in strings
            # make an array that stores the letters of the string
        # store the count in tuple for cuz its a list into the hashmap/dictionary
        # return the values of result in a list

