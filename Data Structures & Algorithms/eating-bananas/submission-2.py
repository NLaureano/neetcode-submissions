class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxx = max(piles)
        rates = range(1, maxx)
        l, r = 0, len(rates) - 1
        best = maxx
        while l <= r:
            m = (l + r) // 2
            rate = rates[m]
            hours = 0
            for p in piles:
                hours += p // rate if p % rate == 0 else (p // rate) + 1
            print(str(rate) + ": " + str(hours))
            if hours > h:
                l = m + 1
            else: # hours <= h
                best = min(best, rate)
                r = m - 1
        return best
