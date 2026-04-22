class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def bt (numsLeft, res):
            if not numsLeft: 
                arr.append(res)
                # Might need a return
            for i, v in enumerate(numsLeft):
                numsLeftCopy = numsLeft.copy()
                numsLeftCopy.pop(i)
                resCopy = res.copy()
                resCopy.append(v)
                bt(numsLeftCopy, resCopy)
            return
        bt(nums, [])
        return arr