class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep tract of number and indicies

        tracker = {}
        for i, num in enumerate(nums):
            tracker[num] = i

        # go thorugh the array and solve it
        for i in range(len(nums)):
            lookFor = target - nums[i]
            
            if lookFor in tracker and tracker[lookFor] != i:
                return [i, tracker[lookFor]]

        return []