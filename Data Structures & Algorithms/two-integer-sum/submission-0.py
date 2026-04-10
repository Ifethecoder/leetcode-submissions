class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            sumPair = target - num
            if sumPair in seen:
                return [seen[sumPair], idx]
            seen[num] = idx
        
