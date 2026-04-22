class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = set()
        def bt (indexAt, combo):
            if indexAt == len(nums): # Considered final integer already
                combos.add(tuple(combo)) 
                return
            bt(indexAt + 1, combo + [nums[indexAt]])
            bt(indexAt + 1, combo)
        bt(0, [])
        return [list(x) for x in combos]