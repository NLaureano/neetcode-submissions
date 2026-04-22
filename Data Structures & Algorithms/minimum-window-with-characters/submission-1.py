class Solution:
    def minWindow(self, s: str, t: str) -> str:
        skey = {}
        tkey = {}
        for l in s:
            skey[l] = skey.get(l, 0) + 1
        for l in t:
            tkey[l] = tkey.get(l, 0) + 1

        for k, v in tkey.items():
            if skey.get(k, 0) < v: return "" # Impossible

        start = 0
        end = len(s) - 1

        key = {}
        key[s[0]] = 1

        l, r = 0, 0
        minLen = float("inf")
        while l <= len(s):
            passed = True
            for k, v in tkey.items(): #Compare if all letter counts match
                if key.get(k, 0) < v:
                    passed = False
                    break
                
            if passed: # Left to move up
                # Check for minimum
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    start = l
                    end = r
                key[s[l]] -= 1
                l += 1
            else: # Right to move up or stay at farthest point
                if r != len(s) - 1: #Not at final position
                    r += 1
                    key[s[r]] = key.get(s[r], 0) + 1
                else: #Didnt pass @ final pos, return early
                    return s[start:end+1]


        return s[start:end+1]
