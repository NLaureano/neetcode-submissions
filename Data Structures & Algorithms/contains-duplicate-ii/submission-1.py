class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0
        sett = {nums[r]}
        while l < len(nums):
            r += 1
            if abs(l - r) > k:
                sett.remove(nums[l])
                l += 1
            if r < len(nums):
                if nums[r] in sett: 
                    return True
                else:
                    sett.add(nums[r])
        return False