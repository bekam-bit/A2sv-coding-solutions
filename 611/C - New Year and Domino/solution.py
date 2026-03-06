h, w = map(int, input().split())

grid = []
H = [[0] * w for _ in range(h)]
V = [[0] * w for _ in range(h)]

for _ in range(h):
    row = list(input())
    grid.append(row)

q = int(input())
queries = []

for _ in range(q):
    row = list(map(int, input().split()))
    queries.append(row)


for row in range(h):
    for col in range(w - 1):
        if grid[row][col] == "." and grid[row][col+1] == ".":
            H[row][col] = 1

for row in range(h - 1):
    for col in range(w):
        if grid[row][col] == "." and grid[row+1][col] == ".":
            V[row][col] = 1

PH = [[0] * (w + 1) for _ in range(h + 1)] 
PV = [[0] * (w + 1) for _ in range(h + 1)]

for row in range(h):
    for col in range(w):
        PH[row][col] = PH[row - 1][col] + PH[row][col - 1] - PH[row - 1][col - 1] + H[row][col]
        PV[row][col] = PV[row - 1][col] + PV[row][col - 1] - PV[row - 1][col - 1] + V[row][col]

H_sum = 0
V_sum = 0

for query in queries:
    row1, col1 , row2, col2 = query

    row1 -= 1
    col1 -= 1
    row2 -= 1
    col2 -= 1

    H_sum = PH[row2][col2 - 1] - PH[row2][col1 - 1] - PH[row1 - 1][col2 - 1] + PH[row1 - 1][col1 - 1]
    V_sum = PV[row2 - 1][col2] - PV[row2 - 1][col1 - 1] - PV[row1 - 1][col2] + PV[row1 - 1][col1 - 1]

    print(V_sum + H_sum)
 


       
