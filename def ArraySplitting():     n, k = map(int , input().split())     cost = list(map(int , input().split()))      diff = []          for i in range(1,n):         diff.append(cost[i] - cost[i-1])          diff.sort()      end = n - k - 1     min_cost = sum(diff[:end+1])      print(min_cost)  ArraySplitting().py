def ArraySplitting():
    n, k = map(int , input().split())
    cost = list(map(int , input().split()))

    diff = []
    
    for i in range(1,n):
        diff.append(cost[i] - cost[i-1])
    
    diff.sort()

    end = n - k - 1
    min_cost = sum(diff[:end+1])

    print(min_cost)

ArraySplitting()
