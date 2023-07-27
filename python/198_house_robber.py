class Solution:
    def rob(self, nums: list[int]) -> int:

        for i in range(len(nums) - 3, -1, -1):
            print(nums[i])
        return 9999999


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
