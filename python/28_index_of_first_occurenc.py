class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1


solution = Solution()
res = solution.strStr('omytestpp', 'test')
print(res)
