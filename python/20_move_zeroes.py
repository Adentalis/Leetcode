class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        print('tu')
        for i, e in enumerate(nums):
            if nums[i] == 0:
                print(nums)


s = Solution()
s.moveZeroes([0, 2, 3, 0, 0, 8])
