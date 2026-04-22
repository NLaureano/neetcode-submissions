class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = set()
        def bt(index : int, summ : int, combo : list) -> None:
            if summ == target:
                combos.add(tuple(combo))
                return
            
            if summ > target or index == len(nums):
                return

            currNum = nums[index]
            bt(index, summ + currNum, combo + [currNum])
            bt(index + 1, summ, combo)
            return
        bt(0, 0, [])
        return [list(x) for x in combos]