class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        zero_count = 0

        for n in nums:
            if n != 0:
                product = product * n
            else:
                zero_count += 1
            
        result = [0] * len(nums)
        if zero_count > 1:
            return result
        
        for i in range(len(nums)):
            if zero_count != 0:
                if nums[i] != 0:
                    result[i] = 0
                else:
                    result[i] = product
            if zero_count == 0:
                result[i] = product // nums[i]

        return result
