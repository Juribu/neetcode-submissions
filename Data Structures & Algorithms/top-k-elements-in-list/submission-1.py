class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # use a dictionary
        # the keys are the number itself
        # value are the occurances
        # increment value by one if its already there
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
        