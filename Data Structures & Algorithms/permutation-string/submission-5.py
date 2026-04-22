class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length > len(s2):
            return False

        key1 = [0] * 26
        for l in s1:
            key1[ord(l) - ord('a')] += 1
        print(key1)
        left = 0
        right = length
        while right <= len(s2):
            subString = s2[left:right]
            key2 = [0] * 26
            for l in subString:
                key2[ord(l) - ord('a')] += 1
            print(key2)
            
            i = 0
            while i < 26:
                if key1[i] != key2[i]:
                    break
                else:
                    i += 1
            if i == 26:
                return True

            left += 1
            right += 1
        return False