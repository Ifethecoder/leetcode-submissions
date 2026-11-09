class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        use two pointers
        we're only concerned with alphanumeric characters
        while left idx less than right idx, we continue the loop
        """
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True
                