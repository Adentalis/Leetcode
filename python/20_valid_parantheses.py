class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        # better use a map!
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                if c == ')':
                    if stack[len(stack) - 1] == '(':
                        stack.pop()
                    else:
                        return False
                elif c == ']':
                    if stack[len(stack) - 1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[len(stack) - 1] == '{':
                        stack.pop()
                    else:
                        return len(stack) == 0

        return True


s = Solution()
print(s.isValid('()'))
print(s.isValid('()[]{}'))
print(s.isValid('[(}]'))
