class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        for s in strs:
            sortedS = str(sorted(s))
            if sortedS not in mapp:
                mapp[sortedS] = []
            mapp[sortedS].append(s)
        return list(mapp.values())