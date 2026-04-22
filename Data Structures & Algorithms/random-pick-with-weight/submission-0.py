import random
class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        for i, n in enumerate(w):
            for _ in range(n):
                self.arr.append(i)
        self.size = len(self.arr)

    def pickIndex(self) -> int:
        index = random.randint(0, self.size - 1)
        return self.arr[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()