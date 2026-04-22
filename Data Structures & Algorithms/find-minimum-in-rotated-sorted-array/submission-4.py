class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        curMin = float("inf")
        while left < right:
            middle = right - ((right - left) // 2)
            curMin = min(curMin, nums[middle])
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        return min(curMin, nums[left])