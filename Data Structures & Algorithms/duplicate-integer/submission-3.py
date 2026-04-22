class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for v in nums:
            if v in Set:
                return True
            Set.add(v)
        return False
            
         