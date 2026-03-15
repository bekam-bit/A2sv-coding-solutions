def coloringGame():
    tc = int(input())

    for _ in range(tc):
        n = int(input())

        elem = list(map(int, input().split()))

        last = elem[-1]
        total = 0

        for k in range(2,n):
            i = 0
            j = k - 1

            while i < j:
                if elem[i] + elem[j] > elem[k] and elem[i] + elem[j] + elem[k] > last:
                    total += j - i
                    j -= 1
                else:
                    i += 1
        print(total)

coloringGame()