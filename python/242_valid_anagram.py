# 2 possible ways, either map first word, or compare directly
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        chars = set()
        for c in s:
            if c in map:
                map[c] += 1
            else:
                chars.add(c)
                map[c] = 1
        for c in chars:
            if not t.count(c) == map.get(c):
                return False
        return True


s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
print(s.isAnagram('rat', 'car'))
