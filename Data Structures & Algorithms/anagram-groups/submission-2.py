class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for a in s:
                alpha[ord(a) - ord("a")] += 1
            hm[tuple(alpha)].append(s) 
        return hm.values()
