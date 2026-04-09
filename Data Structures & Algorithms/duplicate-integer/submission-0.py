class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        iterate through array
        use set to keep track of nums seen
        return true if num is already in set else false
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False