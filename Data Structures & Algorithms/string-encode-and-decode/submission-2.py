class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "!" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            temp = i
            while s[temp] != "!": #Important to iterate until found
                temp += 1
            wordLength = int(s[i:temp])
            word = s[temp + 1: temp + 1 + wordLength]
            res.append(word)
            i = temp + 1 + wordLength

        return res



