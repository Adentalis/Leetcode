
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        res = []
        for num in nums:
            if res.count(num) == 0:

                if len(res) < 3:
                    res.append(num)
                else:
                    if min(res) < num:
                        res.remove(min(res))
                        res.append(num)

        if len(res) == 3:
            return min(res)
        else:
            return max(res)


s = Solution()
print(s.thirdMax([2, 2, 3, 1, 8, 4, 6]))
print(s.thirdMax([2, 2, 3, 1, 4, 6]))
a = list(set([2, 2, 3, 1, 8, 4, 6]))
a = a.sort()
print('a:')
print(a)
