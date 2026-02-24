def ThisIstheLastTime():
    tc = int(input())

    for _ in range(tc):
        n, k = map(int, input().split())

        casino = []
        for i in range(n):
            casino.append(list(map(int, input().split())))

        sorted_casino = sorted(casino, key= lambda x: (x[0], x[-1]))

        intial = k
        for i in range(len(sorted_casino)):
            real = sorted_casino[i][-1]
            l = sorted_casino[i][0]
            r = sorted_casino[i][1]
            
            if l <= intial <= r and real >= intial:
                intial = real
            
        print(intial)
            
ThisIstheLastTime()
