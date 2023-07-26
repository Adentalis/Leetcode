class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dummy = []
        n1 = set(nums1)
        n2 = set(nums2)
        for num in n1:
            if nums2.count(num):
                dummy.append(num)

        return dummy


s = Solution()
print(s.intersection([4, 9, 9, 5], [1, 2, 3, 4, 5, 6]))
