
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        out = []
        maxIndex = len(temperatures) - 1

        for t in range(len(temperatures)):
            nextIndex = t
            found = False
            while nextIndex < t and not found:
                if temperatures[t] > temperatures[nextIndex] - 1:
                    print(t)


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([30, 40, 50, 60]))
print(s.dailyTemperatures([30, 60, 90]))
