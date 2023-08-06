class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_counter = nums.count(0)
        if zero_counter != 0:
            zeroes_found = 0
            for i in range(len(nums)):

                if nums[i] == 0:
                    zeroes_found += 1

                else:
                    if zeroes_found != 0:
                        nums[i - zeroes_found] = nums[i]
                        nums[i] = 0
        print(nums)


s = Solution()
s.moveZeroes([1, 0, 2, 4, 3, 0, 0, 9, 0, 8])
s.moveZeroes([1, 0])
