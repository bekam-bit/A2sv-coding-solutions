class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        st_health = health - grid[0][0]
        if st_health < 1:
            return False

        queue = deque([(grid[0][0], 0, 0, st_health)])

        visited = [[-1 for _ in range(cols)] for _ in range(rows)]
        visited[0][0] = st_health

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            val, r, c, h = queue.popleft()

            if h < visited[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return True

            for dr, dc in dir:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    
                    next_h = h - grid[nr][nc]
                    
                    if next_h >= 1 and next_h > visited[nr][nc]:
                        visited[nr][nc] = next_h
                        queue.append((grid[nr][nc], nr, nc, next_h))

        return False

