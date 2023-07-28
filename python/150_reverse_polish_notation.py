class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (len(token) > 1 and token[0] == '-'):
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                match token:
                    case '+':
                        stack.append(n1 + n2)
                    case '-':
                        stack.append(n1 - n2)
                    case '*':
                        stack.append(n1 * n2)
                    case '/':
                        stack.append(int(n1 / n2))

        return stack[0]


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
