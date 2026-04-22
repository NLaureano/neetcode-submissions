class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Set = {}
        for i, v in enumerate(nums):
            if (target - v) in Set:
                return [Set[target - v], i]
            Set[v] = i