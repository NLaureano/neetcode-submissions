class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minVal = float("inf")
        while left <= right:
            middle = left + ((right - left) // 2)
            minVal = min(minVal, nums[middle])
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        return minVal