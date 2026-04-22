class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            got = nums[m]
            if got == target:
                return m
            elif got < target:
                l = m + 1
            else:
                r = m - 1
        if nums[l] == target: return l
        return -1