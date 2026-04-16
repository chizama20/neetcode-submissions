class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        areas = []
        

        def dfs(r, c):
            count = 0
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return 0
            if grid[r][c] == 0:
                return 0

            if grid[r][c] == 1: 
                grid[r][c] = 0
                count += 1
                count += dfs(r + 1, c)
                count += dfs(r - 1, c)
                count += dfs(r, c + 1)
                count += dfs(r, c - 1)
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    areas.append(area)
        
        if not areas:
            return 0
        areas.sort()
        return areas.pop()