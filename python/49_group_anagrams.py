class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        for word in strs:
            print(word)
            if len(res) == 0:
                res.append([word])

            else:
                i = 0
                found = False
                for group in res:
                    if self.isAnagram(word, group[i]):
                        group.append(word)
                        found = True

                if found == False:
                    res.append([word])

                i += 1

        return res

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
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
