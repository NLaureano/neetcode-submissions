class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        rain = 0
        while left < right:
            curr = None
            if maxLeft <= maxRight:
                left += 1
                rain += max(0, min(maxLeft, maxRight) - height[left])
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                rain += max(0, min(maxLeft, maxRight) - height[right])
                maxRight = max(maxRight, height[right])
        return rain