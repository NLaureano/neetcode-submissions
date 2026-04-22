class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ret = []
        mapp = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
        
        def backtrack(i, currstr):
            if len(currstr) == len(digits):
                ret.append(currstr)
                return
            dig = digits[i]
            chars = mapp[dig]
            for c in chars:
                backtrack(i + 1, currstr + c)
        
        backtrack(0, "")
        return ret