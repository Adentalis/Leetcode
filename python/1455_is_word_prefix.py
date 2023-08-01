class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i in range(len(words)):

            if words[i].startswith(searchWord):
                return i + 1

        return -1


s = Solution()
print(s.isPrefixOfWord(sentence="i love eating burger", searchWord="burg"))
print(s.isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro"))
print(s.isPrefixOfWord(sentence="i am tired", searchWord="you"))
