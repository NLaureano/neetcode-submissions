class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def bt(combo, sumSoFar, start):
            if sumSoFar == target:
                ret.append(combo)
                return
            if sumSoFar > target:
                return

            for i in range(start, len(nums)):
                num = nums[i]
                # Reuse allowed: i instead of i + 1
                bt(combo + [num], sumSoFar + num, i)

        bt([], 0, 0)
        return ret