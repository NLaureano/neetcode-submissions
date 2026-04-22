class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            row = (l + r) // 2
            left = matrix[row][0]
            right = matrix[row][-1]
            if left <= target <= right:
                break
            elif right < target: #Move up rows
                l = row + 1
            else:
                r = row - 1
        l, r = 0, len(matrix[row]) - 1
        col = 0
        while l <= r:
            col = (l + r) // 2
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target: # Move forward
                l = col + 1
            else:
                r = col - 1
        return False 
