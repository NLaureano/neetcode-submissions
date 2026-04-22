class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = []
        for i in s:
            if i.isalnum() == True:
                alphaNum.append(i.lower())
        length = len(alphaNum)
        left = 0
        right = length - 1
        for j in range(length // 2):
            if alphaNum[left] != alphaNum[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


            