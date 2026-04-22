class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = {}
        colmap = {}
        gridmap = {}
        grids = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                grid = grids[row // 3][ col // 3]
                if value != ".":
                    if row not in rowmap: rowmap[row] = set()
                    if col not in colmap: colmap[col] = set()
                    if grid not in gridmap: gridmap[grid] = set()
                    if (value not in rowmap[row]) and \
                        (value not in colmap[col]) and \
                        (value not in gridmap[grid]):
                        rowmap[row].add(value)
                        colmap[col].add(value)
                        gridmap[grid].add(value)
                    else:
                        return False
        return True

