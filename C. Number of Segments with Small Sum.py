def goodSegment():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    cur_len = 0
    total_len = 0
    cur_sum = 0
    
    for right in range(n):
        cur_sum += arr[right]

        while cur_sum > s:
            cur_sum -= arr[left]
            left += 1
        
        if cur_sum <= s:
            cur_len = right - left + 1
            total_len += cur_len
            
    print(total_len)

goodSegment()
