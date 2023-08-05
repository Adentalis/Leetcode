class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 1) use count
        num_set = set(nums)
        for num in num_set:
            if nums.count(num) >= len(nums) / 2:
                return num

    def majorityElement2(self, nums: list[int]) -> int:
        # 2) use a map
        if len(nums) == 1:
            return nums[0]
        dict = {}
        for num in nums:
            if num in dict:
                if dict[num] + 1 >= len(nums) / 2:
                    return num
                else:
                    dict[num] += 1

            else:
                dict[num] = 1
        pass


s = Solution()
print(s.majorityElement2([3, 2, 3]))
print(s.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
