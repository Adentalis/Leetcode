class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        res = []

        for word in words:
            low = word.casefold()
            err = False
            if low[0] in first_row:
                for i in range(1, len(low)):
                    if not low[i] in first_row:
                        err = True
                        break
                if not err:
                    res.append(word)
            elif low[0] in second_row:
                for i in range(1, len(low)):
                    if not low[i] in second_row:
                        err = True
                        break
                if not err:
                    res.append(word)
            else:
                for i in range(1, len(low)):
                    if not low[i] in third_row:
                        err = True
                        break
                if not err:
                    res.append(word)

        return res


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(s.findWords(["omk"]))
print(s.findWords(["adsdf", "sfd"]))
