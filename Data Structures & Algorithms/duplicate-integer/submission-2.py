class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = set(nums)
        return len(nums) != len(hashed)
            
         