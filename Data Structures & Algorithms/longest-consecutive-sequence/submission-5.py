class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if it is the start of a sequence

            # if it is start of the sequence
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length = length + 1
                
                longest = max(length, longest)

        return longest
 
        