class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, v in enumerate(nums):
            hashMap[v] = i

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashMap:
                located = hashMap[diff]
                if located != i:
                    return [i, hashMap[diff]]

