# aquire rotten fruit coordinates
# bfs from that coorinate
# accumulate the time as we go

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        time = 0

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # if r == ROWS - 1 and c == COLS - 1:
                    # return time 

                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1                        

                        queue.append((row, col))

            time += 1
                    
        return time if fresh == 0 else -1
        