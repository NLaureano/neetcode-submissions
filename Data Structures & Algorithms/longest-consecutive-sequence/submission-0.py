class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setted = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in setted:
                curr = n
                count = 1
                while curr + 1 in setted:
                    curr += 1
                    count += 1
                res = max(res, count)
        return res