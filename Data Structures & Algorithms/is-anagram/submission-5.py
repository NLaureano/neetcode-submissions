class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for l in s:
            smap[l] = smap.get(l, 0) + 1
        for l in t:
            tmap[l] = tmap.get(l, 0) + 1
        for k, v in smap.items():
            if k not in tmap or tmap[k] != v:
                return False
        for k, v in tmap.items():
            if k not in smap or smap[k] != v:
                return False
        return True