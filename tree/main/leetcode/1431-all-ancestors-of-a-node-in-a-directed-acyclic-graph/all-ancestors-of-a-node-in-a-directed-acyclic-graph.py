class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]
        dic = defaultdict(set)
        
        for from_node, to_node in edges:
            adj_list[from_node].append(to_node)
            incoming[to_node] += 1
        
        queue = deque() 
        for node in range(n):
            if incoming[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            
            for neigh in adj_list[node]:
                dic[neigh] = dic[neigh].union(dic[node], {node})
                incoming[neigh] -= 1

                if incoming[neigh] == 0:
                    queue.append(neigh)

        return [sorted(dic[i]) for i in range(n)]