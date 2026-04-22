class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = []
        for i in range(length - 1):
            count = -1
            foundWarmer = False
            temp = temperatures[i]
            for followingDays in temperatures[i:length]:
                count += 1
                if followingDays > temp:
                    foundWarmer = True
                    break
            if foundWarmer is True:
                res.append(count)
            else:
                res.append(0)
        res.append(0)
        return res
