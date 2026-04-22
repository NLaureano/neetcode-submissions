class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            cprime = c.lower()
            if cprime.isalnum():
                arr.append(ord(cprime))
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True