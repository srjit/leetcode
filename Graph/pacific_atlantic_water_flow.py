
class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        _rows, _cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or (r < 0) or (c < 0) or (r == _rows) or (c == _cols) or heights[r][c] < prevHeight:
                return
            
            visit.add((r,c))
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(_rows-1, c, atlantic, heights[_rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, _cols-1, atlantic, heights[r][cols-1])

        return [x for x in pacific if x in atlantic]
