class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        #Set number:frequency
        for n in nums:
            mapp[n] = mapp.get(n, 0) + 1
        maxFrequency = max(mapp.values())
        newmap = {}
        for key, v in mapp.items():
            if v not in newmap:
                newmap[v] = []
            newmap[v].append(key)
        frequencies = sorted(newmap.keys(), reverse=True)
        print(newmap.items())
        ret = []
        for f in frequencies:
            print(str(f) + " freq ret = " + str(ret))
            if len(ret) < k:
                print(str(len(ret)) + "<" + str(k))
                for v in newmap[f]:
                    ret.append(v)
            else: break
        
        return ret