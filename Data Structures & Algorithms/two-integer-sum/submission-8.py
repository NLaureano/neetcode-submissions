class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashh:
                return [hashh[diff], i]
            hashh[v] = i
        