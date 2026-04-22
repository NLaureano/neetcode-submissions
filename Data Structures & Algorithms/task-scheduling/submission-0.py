class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for c in tasks: #n
            counts[ord(c) - ord('A')] += 1
        heap = []
        for v in counts: #26
            if v > 0:
                heap.append(-v)
        heapq.heapify(heap) #nlogn
        q = collections.deque()
        time = 0
        while q or heap:
            if heap:
                curr = heapq.heappop(heap)
                if curr < -1:
                    q.append((curr + 1, time + n))
            if q and q[0][1] <= time:
                heapq.heappush(heap, q.popleft()[0])
            time += 1
        return time
