def C1709():
    tc = int(input())

    for _ in range(tc):
        n = int(input())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        res=[]
        op_num = 0
        
        changed = False
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
                op_num += 1
                res.extend([3,i+1])
                changed = True
        
        if n == 1 and not changed:
            print(0)
            continue

        elif n == 1 and changed:
            print(1)
            print(res[0], res[1])
            continue
        

        for i in range(n):
            swapped = False
            for j in range(n - i -1):

                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    op_num += 1
                    res.extend([1,j+1])
                    swapped = True
                
                if b[j] > b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
                    op_num += 1
                    res.extend([2,j+1])
                    swapped = True
            
            if not swapped:
                break
        
        print(op_num)
        for i in range(0, len(res), 2):
            print(res[i], res[i + 1])

C1709()
        
