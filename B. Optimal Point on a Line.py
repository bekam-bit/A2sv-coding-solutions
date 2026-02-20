def optimalPoint():
    
    n=int(input())

    sorted_list=sorted(map(int, input().split()))
    
    if n % 2 == 0:
        print(sorted_list[(n-1)//2])
        
    else:
        print(sorted_list[n//2])


optimalPoint()
