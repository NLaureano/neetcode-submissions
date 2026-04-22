class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        layers = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))            
        while q:
            for i in range(len(q)):
                poppedR, poppedC = q.popleft()
                neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for nr, nc in neighbors:
                    r, c = poppedR + nr, poppedC + nc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
            layers += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1  
        return max(layers, 0)
