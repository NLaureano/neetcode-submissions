class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left = 0
        right = length - 1
        for i in range(length):
            s = numbers[left] + numbers[right]
            if target < s:
                right -= 1
            elif target > s:
                left += 1
            else:
                return [left + 1, right + 1]