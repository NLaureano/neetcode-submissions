class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        leftProd = [1] * length
        rightProd = [1] * length
        res = []
        print(leftProd)
        for i in range(1, length):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]
        print(leftProd)
        print(rightProd)
        for j in range(length - 2, -1, -1):
            rightProd[j] = rightProd[j + 1] * nums[j + 1]
        print(rightProd)
        print(res)
        for k in range(length):
            res.append(leftProd[k] * rightProd[k])
        print(res)
        return res
            