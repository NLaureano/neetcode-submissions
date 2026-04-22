class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        ret = False

        def dfs(r, c, checkWord) -> bool:
            if not checkWord:
                return True
            elif r not in range(rows) or c not in range(cols) or board[r][c] != checkWord[0]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = dfs(r, c + 1, checkWord[1:]) or dfs(r + 1, c, checkWord[1:]) or dfs(r, c - 1, checkWord[1:]) or dfs(r - 1, c, checkWord[1:])
            board[r][c] = temp
            return found
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, word):
                    return True
        return ret
