class Solution:
    def climbStairs(self, n: int) -> int:
        def recursion(s: int) -> int:
            if s == 1 or s == 0:
                return 1
            else:
                return recursion(s - 1) + recursion(s - 2)
        return recursion(n)
