class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        while len(s):
            for word in wordDict:
                try:
                    index = s.index(word)
                    print('index', index)
                except:
                    print('err')

        return True


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(s.wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]))
