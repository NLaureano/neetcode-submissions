class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        bestRate = right
        while left <= right:
            k = left + ((right - left) // 2)
            hoursNeeded = 0
            overflow = False
            for pile in piles:
                hoursNeeded += math.ceil(float(pile)/k)
            if hoursNeeded <= h:
                bestRate = k
                right = k - 1
            else:
                left = k + 1
        return bestRate