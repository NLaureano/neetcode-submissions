class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        visited = set()
        distance = 0

        for m in range(len(grid)): #Adds all treasure chests to q
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    q.append((m,n))
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = range(len(grid))
        cols = range(len(grid[0]))
        while q:
            inLevel = len(q)
            for i in range(inLevel):
                currR, currC = q.popleft()
                visited.add((currR, currC))
                grid[currR][currC] = min(grid[currR][currC], distance)
                for nR, nC in neighbors:
                    r = currR + nR
                    c = currC + nC
                    if r in rows and c in cols and grid[r][c] != -1 and grid[r][c] > (distance):
                        q.append((r, c))
            distance += 1
        
