class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_set = set(t)
        for c in t_set:
            if t.count(c) is not s.count(c):
                return c


s = Solution()
print(s.findTheDifference(s="abcd", t="abcde"))
print(s.findTheDifference(s="", t="y"))
