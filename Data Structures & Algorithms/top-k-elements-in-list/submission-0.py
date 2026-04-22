class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        sortedVals = sorted(hm.items(), key=lambda x:x[1])
        res = []
        for i in range(k):
            res.append(sortedVals.pop(len(sortedVals) - 1)[0])
        return res