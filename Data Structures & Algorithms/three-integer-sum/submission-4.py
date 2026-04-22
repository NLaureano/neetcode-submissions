class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        seenBefore = set()
        for l in range(len(nums)):
            left = nums[l]
            if left in seenBefore:
                continue    
            seenBefore.add(left)
            if left > 0:
                break
            
            m = l + 1
            r = len(nums) - 1
            while m < r:
                mid = nums[m]
                right = nums[r]
                summ = left + mid + right
                if summ > 0:
                    r -= 1
                elif summ < 0:
                    m += 1
                else: # == 0
                    ret.append([left, mid, right])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
                

        return ret