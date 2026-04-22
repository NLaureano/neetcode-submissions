class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lane = [(p, s) for p, s in zip(position, speed)]
        lane.sort(reverse=True)
        stack = []

        for pos, spe in lane:
            stack.append((target - pos)/spe)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
                        