class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        paragraph = paragraph.casefold()
        split = paragraph.split(' ')
        for i in range(len(split)):
            split[i] = split[i].replace('!', '').replace('?', '').replace(
                "'", '').replace(',', '').replace(';', '').replace('.', '')
        unique = set(split)
        max_word = ''
        max_count = 0
        for word in unique:
            if word not in banned:
                if split.count(word) > max_count:
                    max_word = word
                    max_count = split.count(word)

        return max_word


s = Solution()
print(s.mostCommonWord(
    paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
print(s.mostCommonWord(paragraph="a.", banned=[]))
