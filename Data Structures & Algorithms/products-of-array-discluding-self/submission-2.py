class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inOrd, postOrd = [0] * len(nums), [0] * len(nums)
        temp = 1
        for i in range(len(nums)):
            inOrd[i] = temp
            temp *= nums[i]
        
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            postOrd[i] = temp
            temp *= nums[i]

        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = inOrd[i] * postOrd[i]
        return ret