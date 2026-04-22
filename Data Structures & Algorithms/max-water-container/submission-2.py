class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]
            maxArea = max(maxArea, (right - left) * min(leftHeight, rightHeight))
            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1
        return maxArea
            
