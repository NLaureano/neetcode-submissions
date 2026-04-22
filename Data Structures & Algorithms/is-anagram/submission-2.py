class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #O(s + t)
            return False

        keyS = [0] * 26
        keyT = [0] * 26
        for v in s: #O(s)
            keyS[ord(v) - ord('a')] += 1
        for v in t: #O(t)
            keyT[ord(v) - ord('a')] += 1
        for i in range(26):
            if keyS[i] != keyT[i]:
                return False
        return True
        
