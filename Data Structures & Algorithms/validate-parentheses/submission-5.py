class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in s:
            match i:
                case '(' | '{' | '[':
                    stack.append(i)
                case ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                case '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                case ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
        return len(stack) == 0