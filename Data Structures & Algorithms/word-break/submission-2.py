class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mapp = {}
        def dp(wordLeft):
            if wordLeft in mapp:
                return mapp[wordLeft]
            if len(wordLeft) == 0:
                return True
            for i in range(1, len(wordLeft)+1):
                wordTest = wordLeft[0:i]
                if wordTest in wordDict:
                    if dp(wordLeft[i:]): 
                        mapp[wordLeft[i:]] = True
                        return True
            mapp[wordLeft] = False
            return False
        return dp(s)
