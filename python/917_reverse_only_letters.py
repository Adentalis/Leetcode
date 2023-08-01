class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = ''
        res = ''
        for c in s:
            if c.isalpha():
                stack += c
        for i in range(len(s)):
            if s[i].isalpha():
                res += stack[-1]
                stack = stack[:-1]
            else:
                res += s[i]

        return res


s = Solution()
print(s.reverseOnlyLetters("ab-cd"))  # "dc-ba"
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
