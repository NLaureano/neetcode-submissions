class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            width = r - l
            leftHeight, rightHeight = heights[l], heights[r]
            minHeight = min(leftHeight, rightHeight)
            maxArea = max(maxArea, minHeight * width)
            if leftHeight < rightHeight:
                l += 1
            else:
                r -= 1
        return maxArea