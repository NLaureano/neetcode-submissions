class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if l < r and not s[l].isalnum():
                l += 1
                continue
            if l < r and not s[r].isalnum(): 
                r -= 1
                continue
            left = s[l].lower()
            right = s[r].lower()
            if left == right:
                l += 1
                r -= 1
            else:
                return False
        return True
            