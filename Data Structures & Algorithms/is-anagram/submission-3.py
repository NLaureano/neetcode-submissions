class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted = sorted(s)
        tsorted = sorted(t)
        slen = len(ssorted)
        tlen = len(tsorted)
        if slen == tlen:
            for i in range(slen):
                if ssorted[i] != tsorted[i]:
                    return False
            return True
        else:
            return False
        