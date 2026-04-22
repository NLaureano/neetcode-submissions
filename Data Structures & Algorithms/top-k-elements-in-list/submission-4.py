
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for n in nums:
            mapp[n] = mapp.get(n, 0) + 1 # Count frequency
        lis = mapp.items()
        print(lis)
        lis = sorted(lis, key=lambda x : x[1]) # Sort by frequency
        ret = []
        for _ in range(k): 
            n, f = lis.pop()
            ret.append(n)
        return ret