from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        iterate through array and keep counts of the nums
        and their counts
        move numbers with their counts to heap
        while maintaining size k
        """

        countDict = defaultdict(int)
        
        for num in nums:
            countDict[num] += 1
        
        heap = []

        for num, count in countDict.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
