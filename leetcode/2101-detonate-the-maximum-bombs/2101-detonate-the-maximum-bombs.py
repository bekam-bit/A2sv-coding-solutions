class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]

                c_dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if c_dist <= r1 ** 2:
                    adj[i].append(j)
        
        def bfs(bomb):
            visited = set([bomb])
            queue = deque([bomb])

            while queue:
                node = queue.popleft()

                for neigh in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

            return len(visited)

        max_bombs = 0
        for i in range(n):
            cur_bombs = bfs(i)
            max_bombs = max(max_bombs, cur_bombs)
        
        return max_bombs