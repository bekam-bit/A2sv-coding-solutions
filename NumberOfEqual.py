def NumberOfEqual():
    n , m = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    i = j = 0
    
    num_pairs = 0
    while i < n and j < m:
        
        if arr1[i] < arr2[j]:
            i += 1
            
        elif arr1[i] > arr2[j]:
            j += 1

        else: 
            cur_elem = arr1[i]
            p1 = p2 = 0
            
            while i < n and arr1[i] == cur_elem:
                p1 += 1
                i += 1
            
            while j < m and arr2[j] == cur_elem:
                p2 += 1
                j += 1
            
            num_pairs += p1 * p2
    
    print(num_pairs)

NumberOfEqual()
