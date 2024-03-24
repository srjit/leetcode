class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = {}
        def dfs(r, c):
            if r == N:
                return 0
            if c < 0 or c >= N:
                return float("inf")⁄

            if (r,c) in dp:
                return dp[(r,c)]

            res = matrix[r][c]+ min(
                dfs(r+1, c-1),
                dfs(r+1, c),
                dfs(r+1, c+1)
            )

            dp[(r,c)] = res
            return res

        N = len(matrix)
        min_paths = []
        for c in range(N):
            min_paths.append(dfs(0,c))
        return min(min_paths)
        