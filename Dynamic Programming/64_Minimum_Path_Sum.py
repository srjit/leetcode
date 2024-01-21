from typing import List

class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        cache = {}
        m, n = len(grid), len(grid[0])

        def getmin(r, c):
            
            if r == m-1 and c == n-1:
                return grid[m-1][n-1]            
            if r >= m:
                return float("inf")
            if c >= n:
                return float("inf")
            if (r, c) in cache:
                return cache[(r,c)]
            min_distance = grid[r][c] + min(
                    getmin(r+1, c),
                    getmin(r, c+1)
                )

            cache[(r,c)] = min_distance
            return min_distance

        return getmin(0,0)
        

grid = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid))