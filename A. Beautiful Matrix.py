def beautifulMatrix():
    matrix=[]
    for i in range(5):
        row=list(map(int, input().split()))
        matrix.append(row)

    min_moves=0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                min_moves=abs(i-2) + abs(j-2)
    return min_moves

print(beautifulMatrix())


