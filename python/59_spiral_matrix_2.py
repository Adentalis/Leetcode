class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]

        res = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        # dirs = 'r', 'b', 'l', 't' --> current dir right/bottom/left/top
        dir = 'r'
        i = 0

        while i < n * n:
            res[x][y] = i + 1

            if dir == 'r':
                if y + 1 >= n or res[x][y + 1] != 0:
                    dir = 'b'
                    x += 1
                else:
                    y += 1

                pass
            elif dir == 'b':
                if x + 1 >= n or res[x + 1][y] != 0:
                    dir = 'l'
                    y -= 1
                else:
                    x += 1

                pass
            elif dir == 'l':
                if y - 1 < 0 or res[x][y - 1] != 0:
                    dir = 't'
                    x -= 1
                else:
                    y -= 1

                pass
            else:
                if x - 1 < 0 or res[x - 1][y] != 0:
                    dir = 'r'
                    y += 1
                else:
                    x -= 1

            i += 1

        return res


s = Solution()
print(s.generateMatrix(2))
