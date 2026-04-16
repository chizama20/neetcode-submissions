class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        # visited = set()
        def dfs(grid, r, c): 
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return 
            if grid[r][c] == '0':
                return 

            if grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(grid, r + 1, c)
                dfs(grid, r - 1, c)
                dfs(grid, r, c + 1)
                dfs(grid, r, c - 1)

        for r in range(ROWS):        
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(grid, r, c)            
                    islands += 1 
        
        return islands
            