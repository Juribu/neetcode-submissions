class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0

        l, r = 0, len(heights) -1
        while l < r:
            # measure the area
            area = min(heights[l], heights[r]) * (r - l)
            # compare the area with maxStore
            result = max(result, area)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return result
            
        