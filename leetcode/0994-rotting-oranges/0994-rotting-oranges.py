class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = grid
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 2:
                    q.append((i, j))
                if visited[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if not q:
            return -1

        minutes = -1
        dxn = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            while size > 0:
                x ,y = q.popleft()
                size -= 1
                for dx, dy in dxn:
                    i, j = x + dx, y + dy
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and visited[i][j] == 1:
                        visited[i][j] = 2
                        fresh -= 1
                        q.append((i,j))
            minutes += 1

        if fresh == 0:
            return minutes
        return -1