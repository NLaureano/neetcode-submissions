class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                poppedIndex, poppedHeight = stack.pop()
                maxArea = max(maxArea, poppedHeight * (index - poppedIndex))
                start = poppedIndex
            stack.append((start, height))
        while stack:
            poppedIndex, poppedHeight = stack.pop()
            maxArea = max(maxArea, poppedHeight * (len(heights) - poppedIndex))
        return maxArea