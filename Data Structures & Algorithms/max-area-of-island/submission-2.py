class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set() #Set of tuples (row, col)

        def bfs(r, c) -> int:
            q = collections.deque()
            area = 0
            q.append((r, c))
            while q:
                poppedR, poppedC = q.popleft()
                visited.add((poppedR, poppedC))
                neighbors = [(0, 1), (1, 0), (-1, 0), (0,-1)]
                for nr, nc in neighbors:
                    r = poppedR + nr
                    c = poppedC + nc
                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == 1) and ((r, c) not in visited):
                        area += 1
                        visited.add((r, c))
                        q.append((r, c))
            return area + 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, bfs(row, col))

        return maxArea