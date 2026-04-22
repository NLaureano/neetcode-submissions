class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i in range(ord('a'), ord('z') + 1):
            smap[chr(i)] = 0
            tmap[chr(i)] = 0
        for l in s:
            smap[l] = smap.get(l, 0) + 1
        for l in t:
            tmap[l] = tmap.get(l, 0) + 1
        return smap == tmap