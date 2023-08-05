class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if word[0].isupper():
            # print(word)
            if len(word) == 1 Q
                return True

            return True
        else:
            while len(word) > 1:
                print(word)
                if word[0].isupper():
                    return False
                else:
                    word = word[1:]
            return True


s = Solution()
# print(s.detectCapitalUse('ESA'))
print(s.detectCapitalUse('leetcde'))
# print(s.detectCapitalUse('Google'))
