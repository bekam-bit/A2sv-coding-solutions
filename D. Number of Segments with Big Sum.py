def bigSum():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    cur_cnt = 0
    total_cnt = 0
    cur_sum = 0
    
    for right in range(n):
        cur_sum += arr[right]

        while cur_sum >= s:
            cur_cnt = n - right
            total_cnt += cur_cnt
            cur_sum -= arr[left]
            left += 1
            
    print(total_cnt)

bigSum()
