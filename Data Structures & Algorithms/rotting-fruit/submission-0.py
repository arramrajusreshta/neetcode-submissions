from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        time = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque()

        # Count fresh oranges and enqueue rotten ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        # BFS
        while fresh and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1
