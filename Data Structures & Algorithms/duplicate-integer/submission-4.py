class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set() #O(N) Space
        for v in nums: #O(N)
            if v in sett:
                return True
            sett.add(v)
        return False