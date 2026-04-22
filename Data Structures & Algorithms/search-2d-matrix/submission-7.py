class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs (arr: List[int], tar: int) -> bool:
            left = 0
            right = len(arr) - 1
            while left <= right:
                middle = left + ((right - left) // 2) 
                if arr[middle] < tar:
                    left = middle + 1
                elif arr[middle] > tar:
                    right = middle - 1
                else:
                    return True
            return False
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if matrix[middle][0] <= target and target <= matrix[middle][-1]:
                return bs(matrix[middle], target)
            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False 
