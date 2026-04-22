class Solution:
    def checkNum(self, s: str) -> bool:
        if len(s) > 1:
            return True
        match s:
            case "+":
                return False
            case "-":
                return False
            case "*":
                return False
            case "/":
                return False
        return True
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if self.checkNum(char):
                stack.append(int(char))
            else:
                res = None
                right = stack.pop(-1)
                left = stack.pop(-1)
                print(str(left) + str(right) + char)
                match char:
                    case "+":
                        res = left + right
                    case "-":
                        res = left - right
                    case "*":
                        res = left * right
                    case "/":
                        res = int(left / right)
                stack.append(res)
        return stack.pop(-1)