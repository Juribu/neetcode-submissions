class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store nums and index
        indicies = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in indicies:
                return [indicies[difference], i]

            indicies[n] = i

        return []

