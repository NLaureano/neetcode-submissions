class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapp = {}
        for c in nums:
            mapp[c] = mapp.get(c, 0) + 1
        zeros = mapp.get(0, 0)
        ones = mapp.get(1, 0)
        onesend = zeros + ones
        twos = mapp.get(2, 0)
        twosend = len(nums)
        for i in range(0, zeros):
            print(str(i) + " as 0")
            nums[i] = 0
        for j in range(zeros, onesend):
            print(str(j) + " as 1")
            nums[j] = 1
        for k in range(onesend, twosend):
            print(str(k) + " as 2")
            nums[k] = 2
            