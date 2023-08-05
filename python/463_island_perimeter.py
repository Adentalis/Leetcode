class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row_len = len(grid)
        column_len = len(grid[0])
        res = 0

        for i in range(row_len):
            for j in range(column_len):
                neighbors = 0
                if grid[i][j] == 1:
                    # check top
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        neighbors += 1
                    # check bottom
                    if i + 1 < row_len and grid[i + 1][j] == 1:
                        neighbors += 1
                    # check left
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        neighbors += 1
                    # check right
                    if j + 1 < column_len and grid[i][j + 1] == 1:
                        neighbors += 1
                    res += 4 - neighbors

        return res


s = Solution()
print(s.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
