class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in Set:
                Set.remove(s[left])
                left += 1
            Set.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength