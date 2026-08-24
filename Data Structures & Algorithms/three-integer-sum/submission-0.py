class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort the nums

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l,r = i + 1, len(nums) - 1

            while l < r:
                # see if they add up to 0
                sums = a + nums[l] + nums[r]
                if sums == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sums < 0:
                    l += 1
                else:
                    r -= 1

        return result

        