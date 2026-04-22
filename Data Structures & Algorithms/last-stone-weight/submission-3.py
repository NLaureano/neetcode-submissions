class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            stoneX = heapq.heappop(maxHeap)
            stoneY = heapq.heappop(maxHeap)
            if stoneY > stoneX:
                heapq.heappush(maxHeap, stoneX - stoneY)

        maxHeap.append(0)
        return abs(maxHeap[0])


