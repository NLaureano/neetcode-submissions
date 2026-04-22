class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return -0

        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                row, col = q.popleft()

                for nr, nc in neighbors:
                    r = row + nr
                    c = col + nc

                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == "1") and ((r, c) not in visited):
                        q.append((r,c))
                        visited.add((r, c))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands