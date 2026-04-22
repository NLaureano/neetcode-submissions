class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        maxx, minn = 0, 0
        for n in nums:
            temp = maxx + n
            maxx = max(temp, minn + n, n)
            minn = min(temp, minn + n, n)
            globalMax = max(globalMax, maxx)
        return globalMax