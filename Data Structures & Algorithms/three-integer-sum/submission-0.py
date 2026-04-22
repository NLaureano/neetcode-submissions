class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, value in enumerate(nums):
            if value > 0:
                break
            if index > 0 and value == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                summed = value + nums[left] + nums[right]
                if summed > 0: # too big
                    right -= 1
                elif summed < 0: # too small
                    left += 1
                else: #Diff == target
                    res.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res



