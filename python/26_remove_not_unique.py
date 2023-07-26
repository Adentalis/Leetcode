class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lastUnique = nums[0] - 1
        i = 0
        for num in nums:
            print(f"num: {num} - lastUnique: {lastUnique}")
            if num == lastUnique:
                print('if case')
                nums.pop(i)
            else:
                print('else case')
                lastUnique = num
                i += 1

        print(nums)


s = Solution()
s.removeDuplicates([1, 1, 2, 2, 2, 3, 3, 3, 4])
