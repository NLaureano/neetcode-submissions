class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapp = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if len(mapp) < 1:
                mapp[n] = i
                continue
            if diff in mapp:
                return [mapp[diff] + 1, i + 1]
            else:
                mapp[n] = i
        return