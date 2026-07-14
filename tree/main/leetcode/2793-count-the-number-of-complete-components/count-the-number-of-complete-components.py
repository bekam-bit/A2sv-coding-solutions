class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
     
        visited = set()
        complete_components = 0

        for i in range(n):
            if i in visited:
                continue
            
            queue = deque([i])
            visited.add(i)

            component_nodes = []

            while queue:
                curr = queue.popleft()
                component_nodes.append(curr)

                for neigh in adj[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

            v = len(component_nodes)
            total_edges = 0

            for node in component_nodes:
                total_edges += len(adj[node])
            
            if total_edges == v * (v - 1):
                complete_components += 1
            
        return complete_components
            