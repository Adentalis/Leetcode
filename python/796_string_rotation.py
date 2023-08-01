class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) is not len(goal):
            return False

        for i in range(len(s)):
            s = s[1:].__add__(s[0])
            if s == goal:
                return True

        return False


s = Solution()
print(s.rotateString(s="abcde", goal="cdeab"))
print(s.rotateString(s="abcde", goal="abced"))
