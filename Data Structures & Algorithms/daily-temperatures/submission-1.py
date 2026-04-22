class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #duples of (index, temp)
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                poppedIndex, poppedTemp = stack.pop()
                res[poppedIndex] = index - poppedIndex
            stack.append((index, temp))
        return res
