import sys
sys.setrecursionlimit(2000)

def solve() -> None:
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        mat = [list(input()) for _ in range(n)]
        
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if mat[i][j] == "1":
                    adj[i].append(j)
                else:
                    adj[j].append(i)

        visited = [False] * n
        order = []

        def dfs(v: int) -> None:
            visited[v] = True
            for u in adj[v]:
                if not visited[u]:
                    dfs(u)
            order.append(v)
        
        for v in range(n):
            if not visited[v]:
                dfs(v)
        
        perm = [v + 1 for v in reversed(order)]
        print(*perm)

if __name__ == "__main__":
    solve()