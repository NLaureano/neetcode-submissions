class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        HM = {}
        maxArea = 0

        for right in range(len(s)):
            HM[s[right]] = 1 + HM.get(s[right], 0)
            maxArea = max(maxArea, HM[s[right]])

            if (right - left + 1) > k + maxArea:
                HM[s[left]] -= 1
                left += 1

        return right - left + 1
