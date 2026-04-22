class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowWise = []
        colWise = []
        chunkWise = []
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    rowWise.append((row, val))
                    colWise.append((col, val))
                    chunkWise.append((row // 3, col // 3, val))
        return len(rowWise) == len(set(rowWise)) and len(colWise) == len(set(colWise)) and len(chunkWise) == len(set(chunkWise))