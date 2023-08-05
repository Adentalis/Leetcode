class Solution:
    def topKFrequentOld(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        uniques = set()

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
                uniques.add(num)

        print(counter)

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        
        for num in nums:
            

        print(counter)


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))


sett = set()
print('test')
print(len(sett))
sett.add(3)
print(len(sett))
