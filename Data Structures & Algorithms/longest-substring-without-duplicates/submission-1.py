class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        maxLen = 0
        left = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            maxLen = max(maxLen, right + 1 - left)
        return maxLen
